from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'forums'

urlpatterns = [

    #/forums/
    url(r'^$', views.index, name='index'),

    # /forums/712/
    url(r'^(?P<forum_id>[0-9]+)/$', views.detail, name='detail'),

     #create new topic
    url(r'^create_forum/$', views.create_forum, name='create_forum'),

    #add post
    url(r'^(?P<forum_id>[0-9]+)/create_post/$', views.create_post, name='create_post'),

    #view posts in forum
    url(r'^posts/(?P<filter_by>[a-zA_Z]+)/$', views.posts, name='posts'),

    #display_likes
    url(r'^like/(?P<idy>[0-9]+)/$', views.like, name='like'),

    #delete
    url(r'^delet/(?P<ide>[0-9]+)/$',views.delet,name='delet'),
    url(r'^deletepost/(?P<idee>[0-9]+)/$', views.delete, name='delete'),

]
