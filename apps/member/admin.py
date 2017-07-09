# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile,Education,Country,State,City

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'created_at', 'updated_at',)
@admin.register(Education)
class Educationdmin(admin.ModelAdmin):
	list_display = ('university', 'college', 'course','univ_country',)
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ('country',)
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
	list_display = ('name','city',)
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ('name',)
