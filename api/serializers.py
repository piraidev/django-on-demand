from django.contrib.auth.models import User
from api.models import UserDetails, MentorProfile, MenteeProfile, Mentorship
from rest_framework import serializers

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('email', 'picture', 'linkedin', 'behance', 'twitter', 'instagram', 'facebook', 'youtube', 'description', 'education')

class UserSerializer(serializers.ModelSerializer):
    userDetails = UserDetailsSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'userDetails')

class UserSerializerWithoutAuthData(serializers.ModelSerializer):
    userDetails = UserDetailsSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'userDetails')

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
        