Field
=====
.. code-block:: python

   from mongofire import MongoDB, Field
   db = MongoDB('myAppDatabase')

unset
-----

To unset (delete) field, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'email': Field.unset(),
    })


rename
------

To rename field, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'name': Field.rename('username')
    })
