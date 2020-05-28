from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from on_demand.models import SupplierProfile
from on_demand.serializers import SupplierProfileSerializer


@api_view(['GET', 'PUT'])
def supplier_profile(request, user_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        supplier_profile = SupplierProfile.objects.get(user_id=user_id)
    except SupplierProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        supplier_profile = SupplierProfileSerializer(supplier_profile)
        return Response(supplier_profile.data)

    elif request.method == 'PUT':
        serializer = SupplierProfileSerializer(
            supplier_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
