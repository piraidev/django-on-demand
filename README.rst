==================
 Djando On-Demand
==================

Manage suppliers and consumers in an on-demand marketplace. 
More info about on-demand: https://www.pubnub.com/blog/what-is-the-on-demand-economy/

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

2. Include the Django On Demand URLconf in your project urls.py like this::

    path('ondemand/', include('on_demand.urls')),

3. Run ``python manage.py migrate`` to create the models.

4. Visit http://127.0.0.1:8000/ondemand/ to test the new API.