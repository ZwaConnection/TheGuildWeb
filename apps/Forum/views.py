# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/member/')
def forum(request):
    return render(request, 'forum/forum.html')
@login_required(login_url='/member/')
def topic_page(request):
    return render(request, 'forum/topic_page.html')
@login_required(login_url='/member/')
def posts(request):
    return render(request, 'forum/posts.html')
@login_required(login_url='/member/')
def specific_post_page(request):
    return render(request, 'forum/specific_post_page.html')
@login_required(login_url='/member/')
def post_creation_page(request):
    return render(request, 'forum/post_creation_page.html')
