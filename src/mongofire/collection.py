from typing import Tuple, Any

from pymongo.collection import Collection

from .results import MongoDBDocumentAddResult
from .document import MongoDBDocument
from .query import MongoDBQuery


class MongoDBCollection:
    def __init__(self, collection: Collection) -> None:
        self.mongo = collection

    def document(self, id):
        return MongoDBDocument(self.mongo, id)

    def add(self, data: dict[str, Any]) -> Tuple[MongoDBDocumentAddResult, MongoDBDocument]:
        resutl = MongoDBDocumentAddResult(
            self.mongo.insert_one(data.copy()))
        return (resutl, MongoDBDocument(self.mongo, resutl.id))

    def where(self, field_path, operator, value):
        return MongoDBQuery(self.mongo).where(field_path, operator, value)
