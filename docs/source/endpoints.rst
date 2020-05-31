Endpoints
=========

This section assumes you have added the ``on-demand`` url in `urls.py` as follows::

    path('ondemand/', include('on_demand.urls')),


`on-demand` makes use of `django-rest-framework` to provide the following endpoints, and also to provide serializers for the models.


/search-suppliers
~~~~~~~~~~~~~~~~~

This is a GET endpoint that expects a ``search_term`` parameter in free text. This will fire a lookup in the MentorProfile and UserDetails models in the following properties:

* `UserDetails.description`
* `UserDetails.education`
* `MentorProfile.skills`

The response will be JSON type with a list of MentorProfiles that matched the lookup.


/users/<id>/supplier_profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~



* ``/users/<id>/consumer_profile`` (create, update, retrieve)
* ``/newest-suppliers``
* ``/connection`` (create a connection between supplier and consumer, update, terminate)
