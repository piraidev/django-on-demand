from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from on_demand.models import Connection, ConsumerProfile, SupplierProfile
from on_demand.serializers import ConnectionSerializer, ConsumerProfileSerializer, SupplierProfileSerializer
from on_demand.signals import connection_requested, connection_finished, connection_cancelled, connection_accepted, connection_rejected
from django.conf import settings


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'supplier_id', 'consumer_id', 'status')

    def create(self, request, *args, **kwargs):
        objective = request.data['objective']
        if ('consumer_request_comments' in request.data.keys()):
            consumer_request_comments = request.data['consumer_request_comments']
        else:
            consumer_request_comments = None

        if ('connection_status' in request.data.keys()):
            connection_status = request.data['connection_status']
        else:
            connection_status = "STARTED"

        supplier_id = request.data['supplier_id']
        consumer_id = request.data['consumer_id']
        consumer = User.objects.get(id=consumer_id)
        supplier = User.objects.get(id=supplier_id)
        serializer = ConnectionSerializer(data={
            'consumer': consumer.id,
            'supplier': supplier.id,
            'objective': objective,
            'status': connection_status,
            'consumer_request_comments': consumer_request_comments})
        serializer.is_valid()
        connection_created = serializer.save()
        if(connection_created is True):
            connection_requested.send(
                sender=self.__class__, from_user=consumer.profile.email, to_user=supplier.profile.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        connection_id = request.data['connectionId']
        connection_status = request.data['status']
        role = request.data['role']
        connection = Connection.objects.get(id=connection_id)
        connection.status = connection_status
        role_to_notify, user = ('supplier', connection.supplier) if role == 'consumer' else (
            'consumer', connection.consumer)
        from_user = connection.consumer if role == 'consumer' else connection.supplier
        if(connection_status == 'cancelled'):
            connection_cancelled.send(sender=self.__class__, from_user=from_user.profile.email,
                                      to_user=user.profile.email, role_to_notify=role_to_notify, connection_cancelled=connection)
        elif(connection_status == 'finished'):
            ranking = request.data['ranking']
            connection.ranking = ranking
            connection_finished.send(sender=self.__class__, from_user=from_user.profile.email,
                                     to_user=user.profile.email, connection=connection, supplier_ranking=ranking)
        elif(connection_status == 'ongoing'):
            connection_accepted.send(sender=self.__class__, from_user=from_user.profile.email,
                                     to_user=user.profile.email, connection=connection)
        elif(connection_status == 'rejected'):
            rejection_reason = request.data['rejection_reason']
            connection.rejection_reason = rejection_reason
            connection_rejected.send(sender=self.__class__, from_user=from_user.profile.email,
                                     to_user=user.profile.email, connection=connection, rejection_reason=rejection_reason)

        connection.save()
        return Response(status=status.HTTP_200_OK)
