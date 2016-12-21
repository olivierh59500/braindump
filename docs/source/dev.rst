.. toctree::
   :maxdepth: 2
   :caption: Contents:

Development
===========
Braindump is a notes platform written in `Flask`_.

Setting up a local Development Environment
------------------------------------------

The fastest way to get started with braindump development is locally using a virtualenv.

Dependencies
------------
Braindump uses quite a few dependencies and flask extensions.

Common Dependencies
~~~~~~~~~~~~~~~~~~~

.. code::

    # Flask and Extensions
    Flask==0.11.1
    Flask-SQLAlchemy==2.1
    Flask-Script==2.0.5
    Flask-Migrate==2.0.2

    # Utilities and Drivers
    alembic==0.8.9
    psycopg2==2.6.2

Flask
    Flask itself, a microframework for building web applications in Python.

Flask-SQLAlchemy
    Flask Extension for working with the SQLAlchemy ORM

Flask-Script
    Flask Extension for making it easier to extend the Flask CLI

Flask-Migrate
    Flask Extension for dealing with database migrations, utilizing alembic.

Development Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    nose==1.3.7
    sphinx==1.5.1


Code Structure
--------------
The main application source code lives inside of the braindump folder.

.. code::

    .braindump
    ├── controllers
    │   ├── home.py
    │   ├── __init__.py
    ├── forms
    ├── __init__.py
    ├── models
    │   ├── base.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   └── js
    ├── templates
    │   ├── base.html
    │   ├── footer.html
    │   ├── header.html
    │   └── home.html
    └── utils
        └── __init__.py


Controllers
~~~~~~~~~~~

.. automodule:: braindump.controllers
    :members:

Models
~~~~~~

.. automodule:: braindump.models.base
    :members:

.. External Links
.. _Flask: http://flask.pocoo.org/