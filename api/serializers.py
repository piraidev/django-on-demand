from django.contrib.auth.models import User
from api.models import Profile, MentorProfile, MenteeProfile, Message, Mentorship, Notification
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'picture', 'linkedin', 'behance', 'twitter', 'instagram', 'facebook', 'youtube', 'description', 'education')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class UserSerializerWithoutAuthData(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class MentorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = MentorProfile
        fields = ('skills', 'user_id', 'user', 'finished_mentorships_count', 'mentorships_ranking_accumulator')

class MenteeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = MenteeProfile
        fields = ('user_id', 'user')

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
