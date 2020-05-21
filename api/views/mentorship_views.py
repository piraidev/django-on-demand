from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from api.models import Mentorship, MenteeProfile, MentorProfile, Notification
from api.services import notifications_helper
from api.serializers import MentorshipSerializer, MenteeProfileSerializer, MentorProfileSerializer
import api.services.email_service as email_service
from django.conf import settings

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
        notifications_helper.create_notification(mentor_id, mentee_id, 'mentor', 'mentorship_requested', mentorship_created)
        email_service.send_email(mentor.email, settings.SENGRID_REQUEST_TEMPLATE_ID, {'to_name': mentor.first_name, 'from_name': mentee.first_name})
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
            notifications_helper.create_notification(user.id, from_user.id, role_to_notify, 'mentorship_cancelled', mentorship)
            email_service.send_email(user.profile.email, settings.SENGRID_REQUEST_CANCELLED_TEMPLATE_ID, {'to_name': user.first_name, 'from_name': from_user.first_name})
        elif(mentorship_status == 'finished'):
            ranking = request.data['ranking']
            mentorship.ranking = ranking
            notifications_helper.create_notification(user.id, from_user.id, role_to_notify, 'mentorship_finished', mentorship)
            email_service.send_email(user.profile.email, settings.SENGRID_REQUEST_FINISHED_MENTOR_TEMPLATE_ID, {'to_name': user.first_name, 'from_name': from_user.first_name, 'mentor_ranking': ranking})
            email_service.send_email(from_user.profile.email, settings.SENGRID_REQUEST_FINISHED_MENTEE_TEMPLATE_ID, {'to_name': from_user.first_name, 'from_name': user.first_name})
        elif(mentorship_status == 'ongoing'):
            notifications_helper.create_notification(mentorship.mentee.id, mentorship.mentor.id, 'mentee', 'mentorship_accepted', mentorship)
            email_service.send_email(user.profile.email, settings.SENGRID_REQUEST_ACCEPTED_TEMPLATE_ID, {'to_name': user.first_name, 'from_name': from_user.first_name})
        elif(mentorship_status == 'rejected'):
            rejection_reason = request.data['rejection_reason']
            mentorship.rejection_reason = rejection_reason
            notifications_helper.create_notification(user.id, from_user.id, role_to_notify, 'mentorship_rejected', mentorship)
            email_service.send_email(user.profile.email, settings.SENGRID_REQUEST_REJECTED_TEMPLATE_ID, {'to_name': user.first_name, 'from_name': from_user.first_name, 'rejection_reason': rejection_reason})
        
        mentorship.save()
        return Response(status=status.HTTP_200_OK)