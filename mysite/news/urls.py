from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'news'

urlpatterns = [

    #/news/
    url(r'^$', views.index, name='index'),

    # /news/712/
    url(r'^(?P<info_id>[0-9]+)/$', views.detail, name='detail')

]
