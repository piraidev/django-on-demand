from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from api.models import Mentorship, MenteeProfile, MentorProfile
from api.serializers import MentorshipSerializer, MenteeProfileSerializer, MentorProfileSerializer
from django.conf import settings
from api.signals import mentorship_requested, mentorship_finished, mentorship_cancelled, mentorship_accepted, mentorship_rejected

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'mentor_id', 'mentee_id', 'status')

    def create(self, request, *args, **kwargs):
        objective = request.data['objective']
        objective = request.data['objective']
        mentorship_status = request.data['status']
        if ('mentee_request_comments' in request.data.keys()):
            mentee_request_comments = request.data['mentee_request_comments']
        else:
            mentee_request_comments = None
        mentor_id = request.data['mentor_id']
        mentee_id = request.data['mentee_id']
        mentee = User.objects.get(id=mentee_id)
        mentor = User.objects.get(id=mentor_id)
        serializer = MentorshipSerializer(data={
            'mentee': mentee.id,
            'mentor': mentor.id,
            'objective': objective,
            'status': mentorship_status,
            'mentee_request_comments': mentee_request_comments})
        serializer.is_valid()
        mentorship_created = serializer.save()
        if(mentorship_created is True):
            mentorship_requested.send(sender=self.__class__, from_user=mentee.profile.email, to_user=mentor.profile.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        mentorship_id = request.data['mentorshipId']
        mentorship_status = request.data['status']
        role = request.data['role']
        mentorship = Mentorship.objects.get(id=mentorship_id)
        mentorship.status = mentorship_status
        role_to_notify, user = ('mentor', mentorship.mentor) if role == 'mentee' else ('mentee', mentorship.mentee)
        from_user = mentorship.mentee if role == 'mentee' else mentorship.mentor
        if(mentorship_status == 'cancelled'):
            mentorship_cancelled.send(sender=self.__class__, from_user=from_user.profile.email, to_user=user.profile.email, role_to_notify=role_to_notify, mentorship_cancelled=mentorship)
        elif(mentorship_status == 'finished'):
            ranking = request.data['ranking']
            mentorship.ranking = ranking
            mentorship_finished.send(sender=self.__class__, from_user=from_user.profile.email, to_user=user.profile.email, mentorship=mentorship, mentor_ranking=ranking)
        elif(mentorship_status == 'ongoing'):
            mentorship_accepted.send(sender=self.__class__, from_user=from_user.profile.email, to_user=user.profile.email, mentorship=mentorship)
        elif(mentorship_status == 'rejected'):
            rejection_reason = request.data['rejection_reason']
            mentorship.rejection_reason = rejection_reason
            mentorship_rejected.send(sender=self.__class__, from_user=from_user.profile.email, to_user=user.profile.email, mentorship=mentorship, rejection_reason=rejection_reason)
        
        mentorship.save()
        return Response(status=status.HTTP_200_OK)