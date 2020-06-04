from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from on_demand.models import SupplierProfile
from on_demand.serializers import SupplierProfileSerializer, UserSerializer
import urllib.parse


@api_view(['GET'])
def newest_suppliers(request):
    """
    Retrieve the five newest suppliers that joined, nesting user data
    """
    supplier_profiles = SupplierProfile.objects.select_related('user').filter(user__first_name__isnull=False, user__last_name__isnull=False,
                                                                              user__details__description__isnull=False).order_by('-date_joined')[:30]
    supplier_serializer = SupplierProfileSerializer(
        supplier_profiles, many=True)
    return Response(supplier_serializer.data)


@api_view(['GET'])
def find_suppliers(request):
    search_term = request.GET.get('search_term')
    decoded_search_term = urllib.parse.unquote(search_term)
    search_query_tables = "SELECT * FROM api_supplier_profile M LEFT JOIN auth_user U ON M.user_id = U.id LEFT JOIN api_userdetails P ON P.user_id = U.id WHERE "
    search_query_names_like = "U.first_name LIKE %s OR U.last_name LIKE %s OR "
    search_query_full_text_profile = "MATCH (P.description) AGAINST (%s IN NATURAL LANGUAGE MODE)"
    complete_search_query = search_query_tables + search_query_names_like + \
        search_query_full_text_profile + search_query_full_text_supplier_profile
    results = SupplierProfile.objects.raw(
        complete_search_query, ['java', 'java', 'java', 'java', decoded_search_term])
    profile_serializer = SupplierProfileSerializer(results, many=True)
    return Response(profile_serializer.data)
