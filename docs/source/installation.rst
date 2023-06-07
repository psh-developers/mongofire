Installation
============

.. note::
    Before installing MongoFire, you first need to install MongoDB on your machine.
    I'm going to install it on a Linux machine if you're on windows or macOS you can
    install it from here `MongoDB installation <https://www.mongodb.com/docs/manual/installation/#mongodb-installation-tutorials>`_

Let's first install MongoDB. You can install it as follows:

.. code-block:: shell

    sudo apt install mongodb

Now let's start MongoDB server

.. code-block:: shell

    sudo systemctl start mongodb  


Let's check if the server is running

.. code-block:: shell

    sudo systemctl status mongodb

If you see ``active (running)``, then everything is fine and you can continue with me.


Now lets install MongoFire. You can install it as follows:

.. code-block:: shell

    pip3 install mongofire
