from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    # url(r'^profile/$', views.ass_profile, name='ass_profile'),
    url(r'^account/$', views.account, name='account'),
    url(r'^associations/$', views.associations, name='associations'),
]
