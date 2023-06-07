import unittest
from mongofire import Field, FieldValue
from mongofire.document import transform_to_mongodb


def MONGO_FILEDS_GLOBAL(): return {
    '$set': {},
    '$unset': {},
    '$rename': {},
    '$inc': {},
    '$addToSet': {},
    '$push': {},
    '$rename': {},
    '$pull': {},
    '$addToSet': {},
}


class FieldTest(unittest.TestCase):
    def test_set(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'name': 'Mohamed',
            'sub_document': {
                'name': 'Mohamed'
            }
        })
        mongo_fields['$set']['name'] = "Mohamed"
        mongo_fields['$set']['sub_document'] = {
            'name': 'Mohamed'
        }
        assert resutl == mongo_fields

    def test_set_merge(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'name': 'Mohamed',
            'sub_document': {
                'name': 'Mohamed'
            }
        }, merge=True)
        mongo_fields['$set']['name'] = "Mohamed"
        mongo_fields['$set']['sub_document.name'] = 'Mohamed'

        assert resutl == mongo_fields

    def test_unset(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'name': Field.unset(),
        })
        mongo_fields['$unset']['name'] = ""
        assert resutl == mongo_fields

    def test_rename(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'name': Field.rename('username'),
        })
        mongo_fields['$rename']['name'] = "username"
        assert resutl == mongo_fields

    def test_increment(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'age': FieldValue.increment(1),
        })
        mongo_fields['$inc']['age'] = 1
        assert resutl == mongo_fields

    def test_decrement(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'age': FieldValue.decrement(10),
        })
        mongo_fields['$inc']['age'] = -10
        assert resutl == mongo_fields

    def test_push(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'languages': FieldValue.push(['English', 'Arabic']),
        })
        mongo_fields['$push']['languages'] = {'$each': ['English', 'Arabic']}
        assert resutl == mongo_fields

    def test_pull(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'languages': FieldValue.pull(['English', 'Arabic']),
        })
        mongo_fields['$pull']['languages'] = {'$in': ['English', 'Arabic']}
        assert resutl == mongo_fields

    def test_add_to_set(self):
        mongo_fields = MONGO_FILEDS_GLOBAL()
        resutl = transform_to_mongodb({
            'languages': FieldValue.add_to_set({'English', 'Arabic', 'Arabic'}),
        })
        resutl['$addToSet']['languages']['$each'] = sorted(
            resutl['$addToSet']['languages']['$each'])
        mongo_fields['$addToSet']['languages'] = {
            '$each': ['Arabic', 'English']}

        assert resutl == mongo_fields


if __name__ == '__main__':
    unittest.main()
