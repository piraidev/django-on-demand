===============
Social Rest API
===============

Social Rest API is a Django app to conduct construction of APIs ment to be used for on-demannd and social apps.

Detailed documentation is in the "docs" directory.

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

3. Run ``python manage.py migrate`` to create the Social Rest API models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an Social API (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ondemand/ to test the new API.