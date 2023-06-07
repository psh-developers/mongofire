from pymongo import MongoClient

from typing import Any, Optional, Sequence, Type, Union
from bson.codec_options import TypeRegistry
from pymongo.typings import _DocumentType


class MongoFire:
    client: MongoClient

    @staticmethod
    def initialize(host: Optional[Union[str, Sequence[str]]] = None,
                   port: Optional[int] = None,
                   document_class: Optional[Type[_DocumentType]] = None,
                   tz_aware: Optional[bool] = None,
                   connect: Optional[bool] = None,
                   type_registry: Optional[TypeRegistry] = None,
                   **kwargs: Any,) -> MongoClient:

        try:
            # To make sure that only one client is connected
            MongoFire.client.close()
        except AttributeError:
            pass
        MongoFire.client = MongoClient(
            host,
            port,
            document_class,
            tz_aware,
            connect,
            type_registry,
            **kwargs,
        )
        return MongoFire()
