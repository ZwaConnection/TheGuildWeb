# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Reply(models.Model):
#     reply = models.TextField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username

class Topic(models.Model):
    name = models.CharField(max_length = 200)
    status = models.BooleanField(default = False )
    description = models.TextField(blank = True )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # replies = models.ForeignKey(Reply, default='', blank=True, null=True)
    reply = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='Topic_owner', default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='Images/Post/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, default='', related_name='Post_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
