MongoDBCollection
=================

.. code-block:: python

    from mongofire import MongoDB

    db = MongoDB('myDatabase')

    coll_ref = db.collection('users')

This is how you can access collections in MongoFire


add
---

Let's add list of users to our users collection

.. code-block:: python

    users = [
        {
            'name': 'Mohamed',
            'age': 20,
        },
        {
            'name': 'Ali',
            'age': 16,
        },
        {
            'name': 'Ahmed',
            'age': 30,
        },
    ]

    for user in users:
        status, doc_ref = coll_ref.add(user)
        print(doc_ref.id, status.acknowledged)

The ``add`` method will generate a random id for each user document if you
want to use a custom id check out the `set <document.html#set>`_ method

where
-----

The ``where`` method will help you work with multiple documents.
You can query for any documents You can update and delete You can do anything.

Let's say you need to add a new field for all users between 13 and 19 years old. You can do this as follows:

.. code-block:: python

    query = coll_ref.where('age', '>', 13)
    query = query.where('age', '<', 19)

    status = query.update({'isTeenager', True})   

If you want to read query data, do the following:

.. code-block:: python

    # read stream
    for teenager in coll_ref.where('isTeenager', '==', True).stream()
        print(teenager.data.to_pretty())

    # read
    for teenager in coll_ref.where('isTeenager', '==', True).get()
        print(teenager.data.to_pretty())

And you can delete like this:

.. code-block:: python

    query = coll_ref.where('isTeenager', '==', True)
    status = query.delete()

These are all query operators that MongoFire support

.. list-table::
    :widths: 30 10 60
    :header-rows: 1

    * - Operater
      - Mongo
      - Description

    * - ``==``
      - ``$eq``
      - equal to

    * - ``!=``
      - ``$ne``
      - not equal to

    * - ``<``                  
      - ``$lt``  
      - less than
    
    * - ``<=``                 
      - ``$lte`` 
      - less than or equal to
    
    * - ``>``                  
      - ``$gt``  
      - greater than
    
    * - ``>=``                 
      - ``$gte`` 
      - greater than or equal to
    
    * - ``array-contains``     
      - ``$all`` 
      - list items contains all list items
    
    * - ``array-contains-any`` 
      - ``$in``  
      - list items contains to any items in the list
    
    * - ``in``                 
      - ``$in``  
      - value equal to any items in the list
    
    * - ``not-in``             
      - ``$nin`` 
      - value not equal to any items in the list


document
--------
If you only want to work with single document, check out the `MongoDBDocument <document.html>`_ class.



