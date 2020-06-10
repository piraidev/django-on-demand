from django.contrib.auth.models import User
from on_demand.models import UserDetails, SupplierProfile, ConsumerProfile, Connection
from rest_framework import serializers


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('email', 'picture', 'linkedin', 'behance', 'twitter',
                  'instagram', 'facebook', 'youtube', 'description')


class UserSerializer(serializers.ModelSerializer):
    userDetails = UserDetailsSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'userDetails')


class SupplierProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SupplierProfile
        fields = ('user_id', 'user',
                  'finished_connections_count', 'connections_ranking_accumulator')


class ConsumerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ConsumerProfile
        fields = ('user_id', 'user')


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id',
                  'supplier',
                  'consumer',
                  'status',
                  'date_created',
                  'date_finished',
                  'objective',
                  'rejection_reason',
                  'consumer_request_comments',
                  'finish_reason',
                  'ranking')

    def create(self, validated_data):
        return Connection.objects.create(**validated_data)
