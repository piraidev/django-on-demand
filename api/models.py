from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class UserDetails(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='details',
        null=True
    )
    email = models.EmailField(unique=True)
    picture = models.TextField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    behance = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

class MentorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='mentor_profile',
        null=True
    )
    skills = models.TextField(blank=True, null=True)
    finished_mentorships_count = models.IntegerField(default=0)
    mentorships_ranking_accumulator = models.IntegerField(default=0)
    date_joined = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'api_mentor_profile'

class MenteeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='mentee_profile',
        null=True
    )
    date_joined = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'api_mentee_profile'

class Mentorship(models.Model):
    status = models.TextField()
    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentorship_mentor')
    mentee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentorship_mentee')
    date_created = models.DateTimeField(default=timezone.now)
    date_finished = models.DateTimeField(blank=True, null=True)
    objective = models.TextField()
    rejection_reason = models.TextField(blank=True, null=True)
    finish_reason = models.TextField(blank=True, null=True)
    mentee_request_comments = models.TextField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)