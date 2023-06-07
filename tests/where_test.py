"""
TODO: Run mongodb server before running this test.
"""

import unittest

from mongofire import MongoFire, MongoDB


DATABASE = 'testing'
COLLECTION = 'users'
DOCS = [
    {
        'name': 'Mohamed',
        'age': 20,
        'hobbies': ['Photography', 'Painting']
    },
    {
        'name': 'Ali',
        'age': 23,
        'hobbies': ['Cooking', 'Writing']
    },
    {
        'name': 'Max',
        'age': 30,
        'hobbies': ['Hiking', 'Yoga']
    }
]


class WhereTest(unittest.TestCase):

    def test_where_equal(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('name', '==', 'Mohamed')
        result = query.get()
        assert len(result) == 1, f'{len(result)} == 1'
        for doc in result:
            assert doc.data.to_dict().get('name') == 'Mohamed'

    def test_where_not_equal(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('name', '!=', 'Mohamed')
        result = query.get()
        assert len(result) == len(DOCS) - \
            1, f'{len(result)} == {len(DOCS) - 1}'
        for doc in result:
            assert doc.data.to_dict().get('name') != 'Mohamed'

    def test_where_less_than(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            result, _ = coll_ref.add(doc)
            assert result.acknowledged

        query = coll_ref.where('age', '<', 30)
        result = query.get()
        assert len(result) == 2, f'{len(result)} == 2'
        for doc in result:
            assert doc.data.to_dict().get('age') < 30

    def test_where_less_than_or_equal(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('age', '<=', 30)
        result = query.get()
        assert len(result) == 3, f'{len(result)} == 3'
        for doc in result:
            assert doc.data.to_dict().get('age') <= 30

    def test_where_greater_than(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('age', '>', 23)
        result = query.get()
        assert len(result) == 1, f'{len(result)} == 1'
        for doc in result:
            assert doc.data.to_dict().get('age') > 23

    def test_where_greater_than_or_equal(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('age', '>=', 23)
        result = query.get()
        assert len(result) == 2, f'{len(result)} == 2'
        for doc in result:
            assert doc.data.to_dict().get('age') >= 23

    def test_where_array_contains(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where(
            'hobbies', 'array-contains', ['Hiking', 'Yoga'])
        result = query.get()

        assert len(result) == 1
        assert result[0].data.to_dict()['name'] == 'Max'

        query = coll_ref.where(
            'hobbies', 'array-contains', ['Yoga'])
        result = query.get()

        assert len(result) == 1
        assert result[0].data.to_dict()['name'] == 'Max'

        query = coll_ref.where(
            'hobbies', 'array-contains', ['Cooking', 'Yoga'])
        result = query.get()

        assert len(result) == 0

    def test_where_array_contains_any(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where(
            'hobbies', 'array-contains-any', ['Hiking', 'Yoga', 'NULL'])
        result = query.get()

        assert len(result) == 1
        assert result[0].data.to_dict()['name'] == 'Max'

        query = coll_ref.where(
            'hobbies', 'array-contains-any', ['NULL'])
        result = query.get()

        assert len(result) == 0

        query = coll_ref.where(
            'hobbies', 'array-contains-any', ['Hiking', 'Cooking'])
        result = query.get()

        assert len(result) == 2
        assert result[0].data.to_dict()['name'] == 'Ali'
        assert result[1].data.to_dict()['name'] == 'Max'

    def test_where_in(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where(
            'name', 'in', ['Max', 'Osama', 'Sara'])
        result = query.get()

        assert len(result) == 1
        assert result[0].data.to_dict()['name'] == 'Max'

        query = coll_ref.where(
            'name', 'in', ['Osama', 'Sara'])
        result = query.get()

        assert len(result) == 0

    def test_where_not_in(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where(
            'name', 'not-in', ['Max', 'Osama', 'Sara'])
        result = query.get()

        assert len(result) == 2
        assert result[0].data.to_dict()['name'] != 'Max'
        assert result[1].data.to_dict()['name'] != 'Max'

        query = coll_ref.where(
            'name', 'not-in', ['Osama', 'Sara'])
        result = query.get()

        assert len(result) == 3

    def test_update_where(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('age', '>=', 23)
        query.update({'gender': 'male'})

        result = query.get()

        assert len(result) == 2
        for doc in result:
            assert doc.data.to_dict()['gender'] == 'male'

        query = coll_ref.where('gender', '==', None)
        result = query.get()
        assert len(result) == 1
        assert result[0].data.to_dict().get('gender') == None
        assert result[0].data.to_dict().get('age') < 23

    def test_delete_where(self):
        MongoFire.initialize()
        db = MongoDB(DATABASE)
        coll_ref = db.collection(COLLECTION)
        coll_ref.mongo.drop()

        for doc in DOCS:
            coll_ref.add(doc)

        query = coll_ref.where('age', '>=', 23)
        query.delete()

        result = query.get()

        query = coll_ref.where('age', '<', 100)
        result = query.get()
        assert len(result) == 1
        assert result[0].data.to_dict().get('age') < 23


if __name__ == '__main__':
    unittest.main()
