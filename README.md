# ![Logo](docs/logo.svg) MongoFire
A simple MongoDB python driver

## Key Features

- Easy MongoDB Queries: Simplify querying MongoDB by providing an intuitive and straightforward interface, making it as simple as working with Firestore.
- Streamlined Updates and Deletions: Perform updates and deletions on MongoDB collections with ease, reducing the complexity of modifying data.

## Installation
```bash
pip3 install mongofire
```

## Usage
You need first to initialize the client in your `main.py` file. 
```python3
from mongofire import MongoDBClient
MongoDBClient.initialize('mongodb://localhost:27017/')
```
And then you can use it on any file in your project like this
```python3
from mongofire import MongoDB
db = MongoDB('myAppDatabase')
```

I will use this document in the following examples
```python3
document_data =  {
  'name': 'Mohamed',
  'age': 20,
  'emails': [
    'example@gmail.com',
    'example2@gmail.com',
   ],
   'address': {
       'street': 'Schillerplatz',
       'city': 'Hamburg',
       'postal_code': '80331',
       'country': 'Germany'
   }
}
```

### Add document
```python3
doc = db.collection('contacts').document('my_custom_document_key').add(document_data)
```
If you don't add a custom key, it will automatically generate a new unique key. And you can access it like this `doc.key`
