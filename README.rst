==================
 Djando On-Demand
==================

Manage suppliers and consumers in an on-demand marketplace. 
Think of it like an API to build services like Airbnb, Upwork, or any marketplace where you have suppliers offering a service or product, and consumers searching for specific characteristics of the product or service.

This app provides models and API endpoints to facilitate the implementation of the marketplace.

Full documentation on https://django-on-demand.readthedocs.io/en/latest/

Endpoints
---------

* ``/search-suppliers``
* ``/users/<id>/supplier_profile`` (create, update, retrieve)
* ``/users/<id>/consumer_profile`` (create, update, retrieve)
* ``/newest-suppliers``
* ``/connection`` (create a connection between supplier and consumer, update, terminate)


Quick start
-----------

1. This app is using `django-rest-framework` to provide API endpoints, which means this app will need to be added to the list of installed apps.
The app will automatically install `django-rest-framework` if it's not installed.
`on_demand` also needs to be added to the list of installed apps::

    INSTALLED_APPS = [
        ...
        'on_demand',
        'rest_framework'
    ]

Given that the app has models, a db client should be installed. For example `pip install mysqlclient`

2. Include the Django On Demand URLconf in your project urls.py like this::

    path('ondemand/', include('on_demand.urls')),

3. Run ``python manage.py migrate`` to create the models.

4. Visit http://127.0.0.1:8000/ondemand/ to test the new API.