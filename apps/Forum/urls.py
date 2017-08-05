from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.forum, name = 'forum'),
    url(r'^topic_page/$', views.topic_page, name = 'topic_page'),
    url(r'^posts/$', views.posts, name = 'posts'),
    url(r'^specific_post_page/$', views.specific_post_page, name = 'specific_post_page'),
    url(r'^post_creation_page/$', views.post_creation_page, name = 'post_creation_page'),

]
