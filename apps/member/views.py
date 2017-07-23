# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from .forms import *

# Create your views here.

def login(request):
    return render(request, 'member/login.html', {})

def profile(request):
    return render(request, 'member/user_profile.html')

def user_register(request):
    if request.method == 'POST':
        f = UserForm()
        f1 = UserProfileForm()
        if f.is_valid() and f1.is_valid():
            user = f.save(commit=False)
            user.is_active = False
            user.save()
            p = UserProfileForm(commit=False)
            p.user = user
            p.save()
            messages.success(request, 'An email has been sent to you to activate your account !')
            return redirect('main:index')
        else:
            messages.success(request, 'Please , correct the errors below !')
    else:
        f = UserForm()
        f1 = UserProfileForm()

    return render(request, 'member/register.html', {
        'f':f,
        'f1':f1
    })

def accounts(request):
    return render(request, 'member/accounts.html')

def logout(request):
    auth.logout(request)
    return redirect('main:index')
