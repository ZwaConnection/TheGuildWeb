# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ..member.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_of_creation = models.DateField(auto_now=False, auto_now_add=False, null=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # email = models.EmailField(max_length=254, default="")
    initials = models.CharField(max_length=25, default="")
    logo = models.ImageField(upload_to='Images/Association/logo', blank=True)
    country = models.ForeignKey('member.Country', null=True)
    identifier = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # @receiver(post_save, sender=User)
    # def create_association(sender, instance, created, **kwargs):
    #     if created:
    #         Association.objects.get_or_create(identifier=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_association(sender, instance, **kwargs):
    #     instance.association.save()
