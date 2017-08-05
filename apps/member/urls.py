from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',  auth_views.login, {'template_name': 'member/login.html'}, name='login'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^register/$', views.user_register, name = 'register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^change_password/', views.change_password, name= 'change_password'),
    url(r'^forgot_password/', views.forgot_password, name= 'forgot_password'),
    url(r'^account/$', views.account, name = 'account'),
    url(r'^logout/$', views.logout, name = 'logout'),

]
