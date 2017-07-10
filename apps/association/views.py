# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    context = {}
    return render(request, 'association/register.html', context)

# def ass_profile(request):
#     context = {}
#     return render(request, 'association/profile.html', context)

def account(request):
    context = {}
    return render(request, 'association/account.html', context)
