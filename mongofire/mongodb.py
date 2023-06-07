from pymongo.database import Database

from .mongofire import MongoFire
from .errors import MongoFireError
from .collection import MongoDBCollection


class MongoDB:
    def __init__(self, database) -> None:
        try:
            self.mongo: Database = MongoFire.client[database]
        except AttributeError:
            raise MongoFireError(
                'You need to initialize the server first.') from None

    def collection(self, collection_name):
        return MongoDBCollection(self.mongo[collection_name])
