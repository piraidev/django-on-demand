from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import MentorProfile, User
from api.serializers import MentorProfileSerializer, UserSerializer
import urllib.parse

@api_view(['GET'])
def newest_mentors(request):
    """
    Retrieve the five newest mentors that joined, nesting user data
    """
    mentor_profiles = MentorProfile.objects.select_related('user').filter(user__first_name__isnull=False, user__last_name__isnull=False, education__isnull=False, description__isnull=False, skills__isnull=False).order_by('-date_joined')[:30]
    mentor_serializer = MentorProfileSerializer(mentor_profiles, many=True)
    return Response(mentor_serializer.data)

@api_view(['GET'])
def find_mentors(request):
    search_term = request.GET.get('search_term')
    decoded_search_term = urllib.parse.unquote(search_term)
    search_query_tables = "SELECT * FROM api_mentor_profile M LEFT JOIN api_user U ON M.user_id = U.id WHERE "
    search_query_names_like = "U.first_name LIKE %s OR U.last_name LIKE %s OR "
    search_query_full_text = "MATCH (description,education,skills) AGAINST (%s IN NATURAL LANGUAGE MODE)"
    complete_search_query = search_query_tables + search_query_names_like + search_query_full_text
    results = MentorProfile.objects.raw(complete_search_query, [f'%{decoded_search_term}%', f'%{decoded_search_term}%', decoded_search_term])
    profile_serializer = MentorProfileSerializer(results, many=True)
    return Response(profile_serializer.data)