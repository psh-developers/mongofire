# ![Logo](docs/logo.svg) MongoFire
A simple MongoDB python driver

## Key Features

- __Easy MongoDB Queries:__ Simplify querying MongoDB by providing an intuitive and straightforward interface, making it as simple as working with Firestore.
- __Streamlined Updates and Deletions:__ Perform updates and deletions on MongoDB collections with ease, reducing the complexity of modifying data.
---
## Installation
```bash
pip3 install mongofire
```

## Usage
You need first to initialize the client in your `main.py` file. 
```python3
from mongofire import MongoFire
MongoFire.initialize('mongodb://localhost:27017/')
```
And then you can use it on any file in your project like this
```python3
from mongofire import MongoDB
db = MongoDB('myAppDatabase')
```

### Set a document
To create or overwrite a single document, use the following example:
```python3
data = {
    'name': 'Mohamed',
    'age': 20,
}

db.collection('users').document('my_custom_uid').set(data)
```
If the document does not exist, it will be created. If the document does exist, its contents will be overwritten with the newly provided data, unless you specify that the data should be merged into the existing document, as follows:
```python3
doc_ref = db.collection('users').document('my_custom_uid')

doc_ref.set({'gender': 'male'}, merge=True)
```
### Update a document
If you want to update any field in the document, you can use the update method. You can increment values, push or pull items from the list, rename fields, and more.
```python3
from mongofire import Field, FieldValue
db.collection('users').document('my_uid').update({
    'name': Field.rename('username'),
    'age': FieldValue.increment(1),
})
```
### Add a document
Sometimes the document id doesn't make sense and it's ok to be random in that case you can use the `add` method instead of the `set` method.
```python3
doc_ref = db.collection('users').add({
    'name': 'Max',
    'age': 30,
})
```
You can get the randomly generated id by `doc_ref.id`.

### Delete a document
Delete any document as follows:
```python3
db.collection('users').document('doc_id').delete()
```

## Documentation
If you want to know how to delete or update multiple documents or delve into the lib, read the full documentation at [mongofire.readthedocs.io](https://mongofire.readthedocs.io).

## Contributing
We welcome contributions from the community. To contribute to the library, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes, including tests and documentation.
4. Run the test suite to ensure everything is working correctly.
5. Submit a pull request.

## License
The library is licensed under the __MIT License__. See the __LICENSE__ file for more details.

## Credits
- [__Firestore__](https://firebase.google.com/docs/firestore): Firestore provided inspiration with its simplicity and productivity. Although not directly used as a dependency, it influenced the development of this library.
- [__MongoDB__](https://www.mongodb.com/): MongoDB served as the solution to build something similar to Firestore that is free and open source for all.

## Support
If you have any questions, issues, or suggestions, please open an issue on the GitHub repository or contact the maintainer at pshteam.developers@gmail.com.

## Changelog
- __v1.0.0__ (2023-05-25): first release.

## Roadmap
- __Sub Collection__: add sub collcetions for documents.
