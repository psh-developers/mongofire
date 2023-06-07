from .errors import FieldValueError


class UnsetField:
    pass


class RenameField:
    def __init__(self, value: str) -> None:
        self.value = value


class Field:
    @staticmethod
    def unset() -> UnsetField:
        return UnsetField()

    @staticmethod
    def rename(new_name: str) -> RenameField:
        return RenameField(new_name)


class FieldValueIncrement:
    def __init__(self, value: int) -> None:
        self.value = value


class FieldValueDecrement:
    def __init__(self, value: int) -> None:
        self.value = value * -1


class FieldValuePush:
    def __init__(self, value: list) -> None:
        if isinstance(value, list):
            if len(value) == 1:
                self.value = value
            else:
                self.value = {'$each': value}
        else:
            raise FieldValueError('Value type must be list')


class FieldValuePull:
    def __init__(self, value: list) -> None:
        if isinstance(value, list):
            if len(value) == 1:
                self.value = value
            else:
                self.value = {'$in': value}
        else:
            raise FieldValueError('Value type must be list')


class FieldValueAddToSet:
    def __init__(self, value: set) -> None:
        if isinstance(value, set):
            if len(value) == 1:
                self.value = list(value)
            else:
                self.value = {'$each': list(value)}
        else:
            raise FieldValueError('Value type must be set')


class FieldValue:
    @staticmethod
    def increment(value: int) -> FieldValueIncrement:
        return FieldValueIncrement(value)

    @staticmethod
    def decrement(value: int) -> FieldValueDecrement:
        return FieldValueDecrement(value)

    @staticmethod
    def push(value: list) -> FieldValuePush:
        return FieldValuePush(value)

    @staticmethod
    def pull(value: list) -> FieldValuePull:
        return FieldValuePull(value)

    @staticmethod
    def add_to_set(value: set) -> FieldValueAddToSet:
        return FieldValueAddToSet(value)


def transform_to_mongodb(data: dict, merge=False):
    result = {
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

    for key, value in data.items():
        if isinstance(value, dict):
            sub_dict = transform_to_mongodb(value, merge=merge)

            for mongo_method in result.keys():
                if mongo_method == '$set':
                    if merge:
                        for sub_key, sub_value in sub_dict[mongo_method].items():
                            if sub_value != {}:
                                result[mongo_method][f'{key}.{sub_key}'] = sub_value
                    else:
                        if sub_dict[mongo_method] != {}:
                            result[mongo_method][key] = sub_dict[mongo_method]

                elif mongo_method == '$rename':
                    for sub_key, sub_value in sub_dict[mongo_method].items():
                        result[mongo_method][f'{key}.{sub_key}'] = f'{key}.{sub_value}'

                else:
                    for sub_key, sub_value in sub_dict[mongo_method].items():
                        result[mongo_method][f'{key}.{sub_key}'] = sub_value

        elif isinstance(value, UnsetField):
            result['$unset'][key] = ""

        elif isinstance(value, RenameField):
            result['$rename'][key] = value.value

        elif isinstance(value, FieldValueIncrement):
            result['$inc'][key] = value.value

        elif isinstance(value, FieldValueDecrement):
            result['$inc'][key] = value.value

        elif isinstance(value, FieldValuePush):
            result['$push'][key] = value.value

        elif isinstance(value, FieldValuePull):
            result['$pull'][key] = value.value

        elif isinstance(value, FieldValueAddToSet):
            result['$addToSet'][key] = value.value

        else:
            result['$set'][key] = value

    return result
