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
  date_joined = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'User details: {self.user.last_name}, {self.user.first_name}'



class SupplierProfile(models.Model):
  user = models.OneToOneField(
      settings.AUTH_USER_MODEL,
      on_delete=models.SET_NULL,
      related_name='supplier_profile',
      null=True
  )
  finished_connections_count = models.IntegerField(default=0)
  connections_ranking_accumulator = models.IntegerField(default=0)
  date_joined = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'Supplier: {self.user.last_name}, {self.user.first_name}'

  class Meta:
      db_table = 'on_demand_supplier_profile'


class ConsumerProfile(models.Model):
  user = models.OneToOneField(
      settings.AUTH_USER_MODEL,
      on_delete=models.SET_NULL,
      related_name='consumer_profile',
      null=True
  )
  date_joined = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'Consumer: {self.user.last_name}, {self.user.first_name}'

  class Meta:
      db_table = 'on_demand_consumer_profile'


class Connection(models.Model):
  status = models.TextField()
  supplier = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name='connection_supplier')
  consumer = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name='connection_consumer')
  date_created = models.DateTimeField(default=timezone.now)
  date_finished = models.DateTimeField(blank=True, null=True)
  objective = models.TextField()
  rejection_reason = models.TextField(blank=True, null=True)
  finish_reason = models.TextField(blank=True, null=True)
  consumer_request_comments = models.TextField(blank=True, null=True)
  ranking = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return f'Connection {self.id}. Supplier: {self.supplier.first_name}, {self.supplier.last_name}. Consumer: {self.consumer.first_name}, {self.consumer.last_name}'