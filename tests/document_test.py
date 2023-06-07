"""
TODO: Run mongodb server before running this test.
"""

import unittest

from mongofire import MongoFire, MongoDB, FieldValue


DATABASE = 'testing'
COLLECTION = 'users'


class DocumentTest(unittest.TestCase):

    def test_add(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)

        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        document_data = {
            'name': 'Mohamed',
            'age': 20,
        }
        result, _ = db.collection(COLLECTION).add(document_data)

        assert result.acknowledged and result.id != None, f'{result.acknowledged} and {result.id} != None'

    def test_get(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)

        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        document_data = {
            'name': 'Mohamed',
            'age': 20,
        }
        result, doc_ref = db.collection(COLLECTION).add(document_data)
        data = doc_ref.get()

        assert result.id == data.id and data.data.to_dict(
        ) == document_data, f'{result.id} == {data.id} and {data.data.to_dict()} == {document_data}'

    def test_set(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)

        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        document_data1 = {
            'name': 'Mohamed',
            'age': 20,
        }

        doc_ref = db.collection(COLLECTION).document('custom_id')

        doc_ref.set(document_data1)
        data1 = doc_ref.get().data.to_dict()

        doc_ref.set({
            'age': FieldValue.increment(1),
            'gender': 'male'
        }, merge=True)
        data2 = doc_ref.get().data.to_dict()
        document_data2 = {
            'name': 'Mohamed',
            'age': 21,
            'gender': 'male'
        }

        doc_ref.set(document_data1)
        data3 = doc_ref.get().data.to_dict()

        assert data1 == document_data1 and data2 == document_data2 and data3 == document_data1, f'{data1} == {document_data1} and {data2} == {document_data2} and {data3} == {document_data1}'

    def test_update(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)

        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        document_data1 = {
            'name': 'Mohamed',
            'age': 20,
        }
        id = 'custom_id'
        doc_ref = db.collection(COLLECTION).document(id)

        doc_ref.set(document_data1)
        data1 = doc_ref.get().data.to_dict()

        doc_ref.update({
            'name': 'Mohamed Al Kainai',
            'age': FieldValue.increment(1),
            'gender': 'male',
        })
        data2 = doc_ref.get().data.to_dict()

        document_data2 = {
            'name': 'Mohamed Al Kainai',
            'age': 21,
            'gender': 'male',
        }

        assert data1 == document_data1 and data2 == document_data2

    def test_delete(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)

        db.mongo.drop_collection(COLLECTION)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        document_data = {
            'name': 'Mohamed',
            'age': 20,
        }
        _, doc_ref = db.collection(COLLECTION).add(document_data)
        data1 = doc_ref.get().data.to_dict()
        doc_ref.delete()
        data2 = doc_ref.get()

        assert data1 == document_data and data2 == None, f'{data1} == {document_data} and {data2} == None'


if __name__ == '__main__':
    unittest.main()
