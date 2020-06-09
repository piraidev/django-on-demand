from django.conf.urls import url, include
from rest_framework import routers
from on_demand.views import (status_views,
                             role_view,
                             supplier_profile_views,
                             consumer_profile_views,
                             search_views,
                             connection_views)

router = routers.DefaultRouter(trailing_slash=False)
router.register('connection', connection_views.ConnectionViewSet)

urlpatterns = [
    url('status/', status_views.status),
    url('users/change_role/', role_view.change_role),
    url(r'^users/(?P<user_id>[0-9]+)/supplier-profile',
        supplier_profile_views.supplier_profile, name='supplier-profile'),
    url(r'^users/(?P<user_id>[0-9]+)/consumer-profile',
        consumer_profile_views.consumer_profile, name='consumer-profile'),
    url('newest-suppliers', search_views.newest_suppliers, name='newest-suppliers'),
    url(r'^find-suppliers/$', search_views.find_suppliers, name='find-suppliers'),    # Example: /find-suppliers/?search_term=something_to_search
    url('', include(router.urls))
]
