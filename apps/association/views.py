# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    return render(request, 'association/register.html')

def ass_profile(request):
    return render(request, 'association/profile.html')

def account(request):
    return render(request, 'association/account.html')
