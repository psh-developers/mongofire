MongoFire
=========

You can use MongoFire class to initialize the server. You can do this as follows:

.. code-block:: python

    from mongofire import MongoFire
    MongoFire.initialize('mongodb://localhost:27017/')


You can only initialize the server once, so be sure to use this code in your ``main.py`` file.


.. note::

    If you want to get the mongodb original client, you can do it like this:

    .. code-block:: python

        from mongofire import MongoFire
        client = MongoFire.initialize('mongodb://localhost:27017/')

    You can now use it as a normal `pymongo provider <https://pymongo.readthedocs.io/en/stable/tutorial.html>`_.


After initialize MongoFire, you can now easily access databases from any file in your project using the `MongoDB <mongodb.html>`_ class.

