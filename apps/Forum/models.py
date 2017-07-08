# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 200)
    status = models.BooleanField(default = False )
    description = models.TextField(blank = True )
    created_at = models.DateTimeField('auto_now_add = True')
    updated_at = models.DateTimeField('auto_now = True')
    reply = models.TextField(blank = True)


class Post(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='Post')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
