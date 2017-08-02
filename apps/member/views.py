# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# create a function to resolve email to username
def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

# create a view that authenticate user with email
def login(request):
    context = {}
    # email = request.POST['email']
    # password = request.POST['password']
    # username = get_user(email)
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     if user.is_active:
    #         login(request, user)
    #         return render(request, 'member/user_profile.html')
    #     else:
    #         messages.error(request, 'Please correct the information below')
    return render(request, 'member/login.html', {})

def profile(request):
    return render(request, 'member/user_profile.html')

def user_register(request):
    countries = Country.objects.all()
    country_list = [ c.country for c in countries ]
    if request.method == 'POST':
        f = UserForm(request.POST)
        f1 = UserProfileForm(request.POST)
        if f.is_valid() and f1.is_valid():
            user = f.save(commit=False)
            user.is_active = False
            user.save()
            p = f1.save(commit=False)
            p.user = user
            p.save()
            messages.success(request, 'An email has been sent to you !')
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('member/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('main:index')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        f = UserForm()
        f1 = UserProfileForm()

    return render(request, 'member/register.html', {
        'f':f,
        'f1':f1,
        'country': json.dumps(country_list)
    })

def account(request):
    return render(request, 'member/account.html')

def logout(request):
    auth.logout(request)
    return redirect('main:index')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        return redirect('member:login')
    else:
        return render(request, 'member/account_activation_invalid.html', {})
