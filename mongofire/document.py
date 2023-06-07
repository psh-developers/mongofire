from pymongo.collection import Collection

from .field import transform_to_mongodb

from .results import (
    MongoDBDocumentDeleteResult,
    MongoDBDocumentUpdateResult,
    MongoDBDocumentGetResult
)


class MongoDBDocument:
    def __init__(self, collection: Collection, id) -> None:
        self.collection = collection
        self.id = id

    def get(self, *args):
        select = {'_id': 0}
        if args != []:
            for arg in args:
                select[arg] = 1
        data = self.collection.find_one({'_id': self.id}, select)
        if data != None:
            return MongoDBDocumentGetResult(self.id, data)
        return None

    def update(self, data):
        return MongoDBDocumentUpdateResult(
            self.id,
            self.collection.update_one(
                {'_id': self.id},
                transform_to_mongodb(data)
            )
        )

    def set(self, data, merge=False):
        if merge:
            result = self.collection.update_one(
                {'_id': self.id},
                transform_to_mongodb(data, merge=merge),
                upsert=True,
            )
        else:
            result = self.collection.replace_one(
                {'_id': self.id},
                data,
                upsert=True,
            )

        return MongoDBDocumentUpdateResult(
            self.id,
            result
        )

    def delete(self):
        return MongoDBDocumentDeleteResult(
            self.id,
            self.collection.delete_one({'_id': self.id})
        )
