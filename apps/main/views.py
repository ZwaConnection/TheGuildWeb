# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'app/index.html', context)
def about(request):
    return render(request, 'app/about.html')
def contact(request):
    return render(request, 'app/contact_us.html')
def news(request):
    return render(request, 'app/news.html')
def articles(request):
    return render(request, 'app/articles.html')
def article_page(request):
    return render(request, 'app/article_page.html')
def feedback(request):
    return render(request, 'app/feedback.html')
def announcement_page(request):
    return render(request, 'app/announcement_page.html')
def policy(request):
    return render(request, 'app/policy.html')
def chat(request):
    return render(request, 'app/chat.html')
def terms_conditions(request):
    return render(request, 'app/terms_conditions.html')
