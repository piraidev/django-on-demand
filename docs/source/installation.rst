Installation
============


1. You'll need to install `dango-on-demand` using pip::

    pip install django-on-demand

2. This app is using ``django-rest-framework`` to provide API endpoints, which means the app will need to be added to the list of installed apps.

   The app will automatically install `django-rest-framework` if it's not installed.
   `on_demand` also needs to be added to the list of installed apps::

    #settings.py
    INSTALLED_APPS = [
        ...
        'on_demand',
        'rest_framework'
    ]

3. Include the Django On Demand URLconf in your project urls.py like this::

    #urls.py
    path('ondemand/', include('on_demand.urls')),

4. Given that the app has models, a db client should be installed. For example `pip install mysqlclient`. Run ``python manage.py migrate`` to create the models.


5. Visit http://127.0.0.1:8000/ondemand/ to test the new API.