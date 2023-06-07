FieldValue
==========

.. code-block:: python

   from mongofire import MongoDB, FieldValue
   db = MongoDB('myAppDatabase')

increment
---------

To increment field value, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'age': FieldValue.increment(1),
    })

decrement
---------

To decrement field value, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'salary': FieldValue.decrement(200),
    })

push
----

To add items to field value, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'searchKeywords': FieldValue.push(['google', 'facebook']),
    })

pull
----

To delete items from field value, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'searchKeywords': FieldValue.pull(['google']),
    })

add_to_set
----------

To add items to a field value and ensure that there are no duplicate items, use the following example:

.. code-block:: python
    
    db.collection('users').document('user_id').update({
        'searchKeywords': FieldValue.add_to_set({'google'}),
    })

This will add the keyword ``google`` to the ``searchKeywords`` field if it does not exist otherwise it will be ignored