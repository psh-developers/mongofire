import json
from pymongo.results import UpdateResult, DeleteResult, InsertOneResult


class MongoDBDocumentGetResult:
    def __init__(self, id, data) -> None:
        self.id = id
        self.data = MongoDBDocumentData(data)


class MongoDBDocumentUpdateResult:
    def __init__(self, id, result: UpdateResult) -> None:
        self.id = id if id != None else result.upserted_id
        self.acknowledged = result.acknowledged
        self.upserted_id = result.upserted_id
        self.matched_count = result.matched_count
        self.modified_count = result.modified_count
        self.raw_result = result.raw_result


class MongoDBDocumentAddResult:
    def __init__(self, result: InsertOneResult) -> None:
        self.id = result.inserted_id
        self.acknowledged = result.acknowledged


class MongoDBDocumentDeleteResult:
    def __init__(self, id, result: DeleteResult) -> None:
        self.id = id
        self.acknowledged = result.acknowledged
        self.deleted_count = result.deleted_count
        self.raw_result = result.raw_result


class MongoDBDocumentData:
    def __init__(self, data) -> None:
        self.__data: dict = data

    def to_dict(self) -> dict:
        return self.__data

    def to_pretty(self) -> str:
        return json.dumps(self.to_dict, indent=4, ensure_ascii=False)

    def to_json(self) -> str:
        return json.dumps(self.to_dict)
