Quick start
===========

You need first to initialize the client in your ``main.py`` file:

.. code-block:: python

   from mongofire import MongoFire
   MongoFire.initialize('mongodb://localhost:27017/')

And then you can use it in any file in your project like this:

.. code-block:: python

   from mongofire import MongoDB
   db = MongoDB('myAppDatabase')

Set a Document
--------------

.. include:: usage/document.rst
   :start-after: 
      set
      ---
   :end-before:
      update
      ------

Update a Document
-----------------

.. include:: usage/document.rst
   :start-after: 
      update
      ------
   :end-before:
      .. end_update_quick_srart

Add a Document
--------------

Sometimes the document ID doesn't make sense, and it's okay to be random. In that case, you can use the ``add`` method instead of the ``set`` method.

.. code-block:: python

   status, doc_ref = db.collection('users').add({
       'name': 'Max',
       'age': 30,
   })

You can get the randomly generated ID by ``doc_ref.id``.

Delete a Document
-----------------

.. include:: usage/document.rst
   :start-after: 
      delete
      ------
   :end-before:
      .. end_delete_quick_srart

