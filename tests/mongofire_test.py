"""
TODO: Run mongodb server before running this test.
"""

import unittest

from mongofire import MongoFire, MongoDB


DATABASE = 'testing'
COLLECTION = 'users'


class MongoFireTest(unittest.TestCase):
    def test_initialize(self):
        MongoFire.initialize()
        assert MongoFire.client != None

    def test_drop_collection(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()
        assert coll_ref.mongo.find_one() == None


if __name__ == '__main__':
    unittest.main()
