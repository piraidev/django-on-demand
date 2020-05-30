# DJANGO ON-DEMAND

Manage suppliers and consumers in an on-demand marketplace. 
Think of it like an API to build services like Airbnb, Upwork, or any marketplace where you have suppliers offering a service o product, and consumers searching for specific characteristics of the product or service.

More info about on-demand: https://www.pubnub.com/blog/what-is-the-on-demand-economy/

This app provides models and API endpoints to facilitate the implementation of the marketplace.


Yes, fork it.

Please, contribute.
Thanks!

Full documentation on https://django-on-demand.readthedocs.io/en/latest/

### Endpoints


* ``/search-suppliers``
* ``/users/<id>/supplier_profile`` (create, update, retrieve)
* ``/users/<id>/consumer_profile`` (create, update, retrieve)
* ``/newest-suppliers``
* ``/connection`` (create a connection between supplier and consumer, update, terminate)


### Install app
This app is still work in progress. To install the work in progress version 
`pip3 install -i https://test.pypi.org/simple/ django-on-demand`

### INSTALLED_APPS requirement
This app is using `django-rest-framework` to provide API endpoints, which means this app will need to be added to the list of installed apps.
The app will automatically install `django-rest-framework` if it's not installed.
`on_demand` also needs to be added to the list of installed apps.
```
 INSTALLED_APPS = [
        ...
        'on_demand',
        'rest_framework'
    ]
```

Run `python3 manage.py migrate` to get the models from the app.

Include the Social Rest API URLconf in your project `urls.py` like this: `path('ondemand/', include('on_demand.urls'))`