Endpoints
=========

This section assumes you have added the ``on-demand`` url in `urls.py` as follows::

    path('ondemand/', include('on_demand.urls')),


`on-demand` makes use of `django-rest-framework` to provide the following endpoints, and also to provide serializers for the models.


/search-suppliers
~~~~~~~~~~~~~~~~~

This is a GET endpoint that expects a ``search_term`` parameter in free text. This will fire a lookup in the UserDetails model in the following property:

* `UserDetails.description`

The response will be JSON type with a list of MentorProfiles that matched the lookup.


/users/<id>/supplier_profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| GET: Retrieves the supplier profile (if exists) for a given user id.
| PUT: Saves/updates the supplier profile (if exists) for a given user id.

/users/<id>/consumer_profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| GET: Retrieves the consumer profile (if exists) for a given user id.
| PUT: Saves/updates the consumer profile (if exists) for a given user id.

/newest-suppliers
~~~~~~~~~~~~~~~~~
| This is a GET endpoint that will return the latest five suppliers that have been added to the database.
| The response will be a JSON list of SupplierProfile models.

/connection
~~~~~~~~~~~
| Manage connections between a suppplier and a consumer.
|
| **POST**: Creates a new connection between a given supplier and consumer, the required parameters are:

    * `supplier_id`
    * `consumer_id`
    * `objective`: The goal of the connection (optional)
    * `consumer_request_comments`: Any comments the consumer added to the connection request (optional)
    * `status`: Status of the connection, it'll be set to STARTED if not sent

| **PUT**: Updates the connection status. Requires the following fields:

    * `connectionId`: the id of the connection to update
    * `status`: the new status for the connection, the accepted statusses can be:
          
        * `cancelled`
        * `finished`: requires a `ranking` param, which is a numeric value given by the consumer.
        * `ongoing`
        * `rejected`: requires a `rejection_reason` which will contain a text value by the supplier explaining why the connection has been rejected
