from django.conf.urls import url

from . import views

#from django.contrib.auth import views as auth_views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^news/$', views.news, name='news'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^article_page/$', views.article_page, name='article_page'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^announcement_page/$', views.announcement_page, name='announcement_page'),
    url(r'^policy/$', views.policy, name='policy'),
    url(r'^terms_conditions/$', views.terms_conditions, name='terms_conditions'),
]
