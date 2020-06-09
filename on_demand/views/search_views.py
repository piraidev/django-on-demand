from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from on_demand.models import SupplierProfile, UserDetails
from on_demand.serializers import SupplierProfileSerializer, UserSerializer
from django.contrib.auth import get_user_model
import urllib.parse

from django.db import connection

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
    # Getting and parsing search term url param
    search_term = request.GET.get('search_term')
    decoded_search_term = urllib.parse.unquote(search_term)

    # Resolving table names to build the sql query
    supplier_profile_db_table = SupplierProfile._meta.db_table
    user_details_db_table = UserDetails._meta.db_table
    django_auth_user_db_table = get_user_model()._meta.db_table

    # Adding FULL TEXT search only if a MYSQL DB is being used
    if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
      search_query_tables = f'SELECT * FROM {supplier_profile_db_table} S LEFT JOIN {django_auth_user_db_table} U ON S.user_id = U.id LEFT JOIN {user_details_db_table} D ON D.user_id = U.id WHERE '
      search_query_names_like = f'U.first_name LIKE \'%%{decoded_search_term}%%\' OR U.last_name LIKE \'%%{decoded_search_term}%%\'' 
      search_query_full_text_supplier_profile = f' OR MATCH (D.description) AGAINST ({decoded_search_term} IN NATURAL LANGUAGE MODE)'
      complete_search_query = search_query_tables + search_query_names_like + search_query_full_text_supplier_profile
    else:
      search_query_tables = f'SELECT * FROM {supplier_profile_db_table} S LEFT JOIN {django_auth_user_db_table} U ON S.user_id = U.id WHERE '
      search_query_names_like = f'U.first_name LIKE \'%%{decoded_search_term}%%\' OR U.last_name LIKE \'%%{decoded_search_term}%%\''
      complete_search_query = search_query_tables + search_query_names_like

    results = SupplierProfile.objects.raw(complete_search_query)

    profile_serializer = SupplierProfileSerializer(results, many=True)
    return Response(profile_serializer.data)
