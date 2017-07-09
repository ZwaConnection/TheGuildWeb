# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at', 'status')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at', 'post_user')
