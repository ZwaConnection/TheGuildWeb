# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Association)

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
	list_display = ('identifier', 'name', 'created_at', 'updated_at',)
