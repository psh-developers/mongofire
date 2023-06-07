Quick start
===========

Installation
------------

.. code-block:: bash

   pip3 install mongofire

Usage
-----

You need to first initialize the client in your `main.py` file:

.. code-block:: python

   from mongofire import MongoFire
   MongoFire.initialize('mongodb://localhost:27017/')

And then you can use it in any file in your project like this:

.. code-block:: python

   from mongofire import MongoDB
   db = MongoDB('myAppDatabase')

Set a Document
--------------

To create or overwrite a single document, use the following example:

.. code-block:: python

   data = {
       'name': 'Mohamed',
       'age': 20,
   }

   db.collection('users').document('my_custom_uid').set(data)

If the document does not exist, it will be created. If the document does exist, its contents will be overwritten with the newly provided data, unless you specify that the data should be merged into the existing document, as follows:

.. code-block:: python

   doc_ref = db.collection('users').document('my_custom_uid')
   doc_ref.set({'gender': 'male'}, merge=True)

Update a Document
-----------------

If you want to update any field in the document, you can use the update method. You can increment values, push or pull items from the list, rename fields, and more.

.. code-block:: python

   from mongofire import Field, FieldValue
   db.collection('users').document('my_uid').update({
       'name': Field.rename('username'),
       'age': FieldValue.increment(1),
   })

Add a Document
--------------

Sometimes the document ID doesn't make sense, and it's okay to be random. In that case, you can use the `add` method instead of the `set` method.

.. code-block:: python

   doc_ref = db.collection('users').add({
       'name': 'Max',
       'age': 30,
   })

You can get the randomly generated ID by `doc_ref.id`.

Delete a Document
-----------------

Delete any document as follows:

.. code-block:: python

   db.collection('users').document('doc_id').delete()

