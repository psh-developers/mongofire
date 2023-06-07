MongoDB
=======

You can access any database from any file in your project as follows:

.. code-block:: python

    from mongofire import MongoDB

    db = MongoDB('MyDatabaseName')


Now with ``db`` object you can do anything. You can read write, delete update, etc.


.. note::

    The ``db`` object contains a mongo object, you can access the original database object of `pymongo <https://pymongo.readthedocs.io/en/stable/tutorial.html#getting-a-database>`_.

    Here is an example of how to do that:

    .. code-block:: python

        db.mongo # < This is Database object for pymongo


Now suppose we have a collection of users in our mongo database and we need to add a new user to it. You can do this as follows:

.. code-block:: python

    from mongofire import MongoDB

    db = MongoDB('MyDatabaseName')

    db.collection("users").document('my_custom_user_id').set(
        {
            'name': 'Mohamed',
            'age': 20,
        }
    )

To understand how ``document`` and ``set`` method works, check out the `MongoDBDocument <document.html>`_ class.

Now suppose we need to get all users older than 18 years old. You can do this as follows:

.. code-block:: python

    from mongofire import MongoDB

    db = MongoDB('MyDatabaseName')

    query = db.collection('users').where('age', '>', 18)

    for user in query.stream():
        print(user.id)
        print(user.data.to_dict())

If you need to understand how collection and queries actually work in MongoFire, check out the `MongoDBCollection <collection.html>`_ class

