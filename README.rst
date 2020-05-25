===============
Social Rest API
===============

Social Rest API is a Django app to conduct construction of APIs ment to be used for on-demannd and social apps.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "social-rest-api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'social-rest-api',
    ]

2. Include the Social Rest API URLconf in your project urls.py like this::

    path('social-rest-api/', include('social-rest-api.urls')),

3. Run ``python manage.py migrate`` to create the Social Rest API models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an Social API (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/social-rest-api/ to test the new API.