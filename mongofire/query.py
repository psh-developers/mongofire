from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.results import UpdateResult
from .results import MongoDBDocumentGetResult
from .document import transform_to_mongodb


class Query:
    DESCENDING = -1
    ASCENDING = 1


class MongoDBCursor(Cursor):
    def __init__(self, collection, *args, **kwargs):
        super().__init__(collection, *args, **kwargs)

    def __next__(self) -> MongoDBDocumentGetResult:
        document = super().__next__()
        id = document['_id']
        del document['_id']

        return MongoDBDocumentGetResult(id, document)


class MongoDBQuery:
    def __init__(self, collection: Collection) -> None:
        self.__collcetion: Collection = collection
        self.__queries = {}
        self.__limit: int = None
        self.__skip: int = None
        self.__order_by: tuple[str, int] = None

    def where(self, field_path, operator, value):
        self.__queries[field_path] = {_convert_operator(operator): value}
        return self

    def limit(self, value: int):
        self.__limit = value
        return self

    def skip(self, value: int):
        self.__skip = value
        return self

    def order_by(self, field_path: str, direction=Query.ASCENDING):
        self.__order_by = (field_path, direction)
        return self

    def stream(self) -> MongoDBCursor:
        cursor = MongoDBCursor(self.__collcetion, self.__queries)
        if self.__order_by is not None:
            cursor.sort(*self.__order_by)
        if self.__skip is not None:
            cursor.skip(self.__skip)
        if self.__skip is not None:
            cursor.limit(self.__limit)

        return cursor

    def get(self) -> tuple[MongoDBDocumentGetResult]:
        return tuple(self.stream())

    def update(self, data: dict) -> UpdateResult:
        return self.__collcetion.update_many(self.__queries, transform_to_mongodb(data, merge=True))

    def delete(self):
        return self.__collcetion.delete_many(self.__queries)


def _convert_operator(operator):
    mapping = {
        '==': '$eq',
        '<': '$lt',
        '<=': '$lte',
        '>': '$gt',
        '>=': '$gte',
        '!=': '$ne',
        'array-contains': '$all',
        'array-contains-any': '$in',
        'in': '$in',
        'not-in': '$nin'
    }
    return mapping.get(operator, operator)
