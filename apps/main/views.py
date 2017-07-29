# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'app/index.html', context)
def about(request):
    context = {}
    return render(request, 'app/about.html',context)
def contact(request):
    context = {}
    return render(request, 'app/contact_us.html',context)
def news(request):
    context = {}
    return render(request, 'app/news.html',context)
def articles(request):
    context = {}
    return render(request, 'app/articles.html',context)
def article_page(request):
    context = {}
    return render(request, 'app/article_page.html',context)
def feedback(request):
    context = {}
    return render(request, 'app/feedback.html',context)
def policy(request):
    context = {}
    return render(request, 'app/policy.html',context)
def chat(request):
    context = {}
    return render(request, 'app/chat.html',context)
def terms_conditions(request):
    context = {}
    return render(request, 'app/terms_conditions.html',context)
def announcements(request):
    context = {}
    return render(request, 'app/announcements.html',context)
