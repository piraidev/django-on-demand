from django.conf.urls import url, include
from rest_framework import routers
from api.views import (views,
                       role_view,
                       mentor_profile_views,
                       mentee_profile_views,
                       search_views,
                       mentorship_views)

router = routers.DefaultRouter(trailing_slash=False)
router.register('mentorship', mentorship_views.MentorshipViewSet)

urlpatterns = [
    url('status/', views.status),
    url('users/change_role/', role_view.change_role),
    url(r'^users/(?P<user_id>[0-9]+)/mentor_profile', mentor_profile_views.mentor_profile),
    url(r'^users/(?P<user_id>[0-9]+)/mentee_profile', mentee_profile_views.mentee_profile),
    url('newest_mentors', search_views.newest_mentors),
    url(r'^find-mentors/$', search_views.find_mentors),
    url('', include(router.urls))
]