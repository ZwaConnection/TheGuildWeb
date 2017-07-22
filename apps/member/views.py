# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import auth

from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'member/login.html', {})

def profile(request):
    return render(request, 'member/user_profile.html')

def user_register(request):
    return render(request, 'member/register.html', {})

def accounts(request):
    return render(request, 'member/accounts.html')

def logout(request):
    auth.logout(request)
    return redirect('main:index')
