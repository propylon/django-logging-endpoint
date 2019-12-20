django-logging-endpoint
=======================

> Provide an endpoint to receive logs and push them to a configurable django logger

.. image:: https://travis-ci.org/propylon/django-logging-endpoint.svg?branch=master
    :target: https://travis-ci.org/propylon/django-logging-endpoint

Usage
-----

Installation
************
1. Install the package::

    pip install django-logging-endpoint

2. Install the application by adding it to the INSTALLED_APPS setting::

    INSTALLED_APPS += ('logging_endpoint',)

3. Set the logger name, if you want to send the messages to a specific one::

    LOGGING_ENDPOINT_LOGGER = 'LoggingEndpoint'

4. Set the log message handler function, if you want to customize the parsing of your log messages::

    LOGGING_ENDPOINT_MESSAGE_HANDLER = 'logging_endpoint.message_handler.default_handler'

5. Add the url to your urls.py::

    from django.conf.urls import include

    urlpatterns += url(r'^logs', include('logging_endpoint.urls'))

Endpoints
*********

root
^^^^
The root endpoint of :code:`django-logging-endpoint` receives a json message
with the logs to be sent to the configured logger::

    {
        'message':   'my log message',
        'logger':    'user interaction',
        'loglevel':  'error',
        'timestamp': '2020-01-01T12:00Z'
    }

By default, a list of logs can be received and will be expanded to the Django
logger. See the documentation's settings chapter for more information on that.

Development
-----------

Makefile
********

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Tests
* `make plain-test` - Run Tests without rebuilding the project
* `make sdist` - Build a Python source distribution
* `make docs` - Build the Sphinx documentation
* `make lint` - Get a codestyle report about your code
* `make plain-lint` - Get a codestyle report without rebuilding the project
* `make` - Equivalent to `make test lint docs sdist`
