from api.models import User, MentorProfile, MenteeProfile, Message, Mentorship, Notification
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'created')

class UserSerializer(serializers.ModelSerializer):
    auth_token = TokenSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'auth_token', 'first_name', 'last_name', 'picture', 'linkedin', 'behance', 'twitter', 'instagram', 'facebook', 'youtube')

class UserSerializerWithoutAuthData(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'picture', 'linkedin', 'behance', 'twitter', 'instagram', 'facebook', 'youtube')

class MentorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = MentorProfile
        fields = ('description', 'education', 'skills', 'user_id', 'user', 'finished_mentorships_count', 'mentorships_ranking_accumulator')

class MenteeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = MenteeProfile
        fields = ('description', 'education', 'user_id', 'user')

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializerWithoutAuthData(read_only = True)
    class Meta:
        model = Message
        fields = ('mentorship', 'sender', 'text', 'date_sent')

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ('id',
                  'mentor',
                  'mentee',
                  'status',
                  'date_created',
                  'date_finished',
                  'objective',
                  'rejection_reason',
                  'mentee_request_comments',
                  'finish_reason',
                  'ranking')

    def create(self, validated_data):
        return Mentorship.objects.create(**validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializerWithoutAuthData(read_only = True)
    from_user = UserSerializerWithoutAuthData(read_only = True)
    class Meta:
        model = Notification
        fields = ('id', 'user', 'from_user', 'mentorship', 'notification_type', 'date_created', 'viewed')
