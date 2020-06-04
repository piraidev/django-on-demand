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
    url(r'^users/(?P<user_id>[0-9]+)/supplier_profile',
        supplier_profile_views.supplier_profile),
    url(r'^users/(?P<user_id>[0-9]+)/consumer_profile',
        consumer_profile_views.consumer_profile),
    url('newest-suppliers', search_views.newest_suppliers),
    url(r'^find-suppliers/$', search_views.find_suppliers),
    url('', include(router.urls))
]
