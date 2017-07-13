from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^user_register/$', views.user_register, name = 'user_register'),
    url(r'^accounts/$', views.accounts, name = 'accounts'),
    url(r'^logout/$', views.logout, name = 'logout'),

]
