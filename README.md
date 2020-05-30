# DJANGO ON-DEMAND

[![pypi-version]][pypi]

[pypi-version]: https://img.shields.io/pypi/v/django-on-demand.svg
[pypi]: https://pypi.org/project/django-on-demand/

Manage suppliers and consumers in an on-demand marketplace. 
More info about on-demand: https://www.pubnub.com/blog/what-is-the-on-demand-economy/

Yes, fork it.

Please, contribute.

Thanks!

Full documentation on https://djangopackages.org/packages/p/django-on-demand/

### Install app
This app is still work in progress. To install the work in progress version 
`pip3 install django-on-demand`

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

Include the Django On Demand Rest API URLconf in your project `urls.py` like this: `path('ondemand/', include('on_demand.urls'))`