# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        form1 = AssociationForm(request.POST)
        form2 = IdentifierForm(request.POST)
        # form2.fields['username'] = form1.data['name']
        # print form2.data['username']
        if form1.is_valid() and form2.is_valid():
            user = form2.save()
            a = form1.save(commit=False)
            a.identifier = user
            a.save()
            messages.success(request, 'You have registered your association successfully')
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

# def ass_profile(request):
#     context = {}
#     return render(request, 'association/profile.html', context)

def account(request):
    context = {}
    return render(request, 'association/account.html', context)

def associations(request):
    context = {}
    return render(request, 'association/associations.html', context)
