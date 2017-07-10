# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html')

def topic_page(request):
    return render(request, 'forum/topic_page.html')

def posts(request):
    return render(request, 'forum/posts.html')

def specific_post_page(request):
    return render(request, 'forum/specific_post_page.html')

def post_creation_page(request):
    return render(request, 'forum/post_creation_page.html')
