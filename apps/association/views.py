# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        form1 = AssociationForm(request.POST)
        form2 = IdentifierForm(request.POST)
        # form2.fields['username'] = form1.data['name']
        # print form2.data['username']
        if form1.is_valid() and form2.is_valid():
            user = form2.save(commit=False)
            user.is_active = False
            user.save()
            a = form1.save(commit=False)
            a.identifier = user
            a.save()
            messages.success(request, 'An email has been sent to you to activate your account !')
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('association/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('main:index')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form1 = AssociationForm()
        form2 = IdentifierForm()

    return render(request, 'association/register.html', {
            'form1': form1,
            'form2': form2
    })

def activate(request, token , uidb64):
    try:
        uid = force_text(urlsafe_base64_encode)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.association.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('main:index')
    else:
        return render(request, 'association/account_activation_invalid.html', {})

def account(request):
    context = {}
    return render(request, 'association/account.html', context)

def associations(request):
    context = {}
    return render(request, 'association/associations.html', context)
