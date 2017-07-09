# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from apps.member.models import Profile

from ..association.models import Association

class Announcement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    date = models.DateField()
    picture = models.ImageField(upload_to='Images/Announcement/picture', blank=True)
    #user = models.ForeignKey(User)
    association = models.ForeignKey(Association)
