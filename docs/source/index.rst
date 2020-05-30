Welcome to django-on-demand's documentation!
============================================

Manage suppliers and consumers in an on-demand marketplace. 
Think of it like an API to build services like Airbnb, Upwork, or any marketplace where you have suppliers offering a service o product, and consumers searching for specific characteristics of the product or service.

This app provides models and API endpoints to facilitate the implementation of the marketplace.

Endpoints
---------

* ``/search-suppliers``
* ``/users/<id>/supplier_profile`` (create, update, retrieve)
* ``/users/<id>/consumer_profile`` (create, update, retrieve)
* ``/newest-suppliers``
* ``/connection`` (create a connection between supplier and consumer, update, terminate)

Content
~~~~~~~

.. toctree::
   :maxdepth: 3
   
   installation
   endpoints
   models
   admin



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
