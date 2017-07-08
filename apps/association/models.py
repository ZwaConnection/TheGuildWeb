# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_of_creation = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
