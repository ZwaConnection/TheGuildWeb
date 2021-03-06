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
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import anonymous_required

# create a function to resolve email to username
def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

# create a view that authenticate user with email
@anonymous_required
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

@login_required(login_url='/member/')
def profile(request):
    return render(request, 'member/user_profile.html')

@anonymous_required
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

@login_required(login_url='/member/')
def account(request):
    if request.method == 'POST':
        u = UpdateUserForm(request.POST, instance=request.user)
        p = UserProfileForm(request.POST, instance=request.user.profile)
        if u.is_valid() and p.is_valid():
            u.save()
            p.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('member:profile')
        else:
            messages.error(request, 'Correct the error below')
    else:
        u = UpdateUserForm(instance=request.user)
        p = UserProfileForm(instance=request.user.profile)
    return render(request, 'member/account.html',{
            'update_form': u,
            'profile_form': p
    })

@login_required(login_url='/member/')
def change_password(request):
    if request.method == 'POST':
        f = PasswordChangeForm(request.user, request.POST)
        if f.is_valid():
            user = f.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully')
            return redirect('member:profile')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        f = PasswordChangeForm(request.user)
    return render(request, 'member/change_password.html',{
        'password_form': f
    })

@anonymous_required
def forgot_password(request):
    if request.method == 'POST':
        f = ForgotPasswordForm(request.POST)
        if f.is_valid():
            print 'Ok'
            messages.success(request, 'An link has been sent to your email address')
        else:
            messages.error(request, 'Your account is not activated')
    else:
        f = ForgotPasswordForm()

    return render (request, 'member/forgot_password.html', {
        'forgot_password_form': f
    })

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
