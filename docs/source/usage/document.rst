MongoDBDocument
===============

.. code-block:: python

   from mongofire import MongoDB
   db = MongoDB('myAppDatabase')

set
---

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


update
------

If you want to update any field in the document, you can use the update method. You can increment values, push or pull items from the list, rename fields, and more.

.. code-block:: python

   from mongofire import Field, FieldValue
   db.collection('users').document('my_uid').update({
       'name': Field.rename('username'),
       'age': FieldValue.increment(1),
   })

.. end_update_quick_srart

To learn more about push, pull, increment, decrement, etc., check out `Field <field.html>`_ and `FieldValue <fieldvalue.html>`_ classes.

get
---

To get single document data, use the following example:

.. code-block:: python

    doc = db.collection('users').document('my_custom_uid').get()
    print(doc.data.to_dict())

To get only specific fields from the document, use the following example:

.. code-block:: python

    doc = db.collection('users').document('my_custom_uid').get('hobbies', 'age')
    print(doc.data.to_dict())


delete
------

Delete any document as follows:

.. code-block:: python

   db.collection('users').document('doc_id').delete()

.. end_delete_quick_srart
