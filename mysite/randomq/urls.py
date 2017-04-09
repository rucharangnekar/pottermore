from django.conf.urls import url
from . import views
from randomq import views
from randomq.views import basic,q

from django.conf import settings
from django.conf.urls.static import static

app_name='randomq'

urlpatterns =[
	url(r'^$',views.basic,name='basic'),
	url(r'^q/$',views.q,name='q'),
	url(r'^cal/$',views.cal,name='cal'),
	url(r'^letter/$',views.letter,name='letter'),
	url(r'^bas/$',views.bas,name='bas'),
	url(r'^leader/$',views.leader,name='leader'),
	url(r'^visitor/$',views.visitor,name='visitor'),
	url(r'^visit/$',views.visit,name='visit'),
	url(r'^level/(?P<cll>[0-9]+)/$', views.level, name='level'),
	url(r'^lcal/(?P<cll>[0-9]+)/$', views.lcal, name='lcal'),
	url(r'^mainquiz/$',views.mainquiz,name='mainquiz'),
	url(r'^spells/(?P<idi>[0-9]+)/$', views.spells, name='spells'),
	url(r'^books/(?P<id2>[0-9]+)/$', views.books, name='books'),
	url(r'^movies/(?P<id3>[0-9]+)/$', views.movies, name='movies'),
	url(r'^quotes/(?P<id4>[0-9]+)/$', views.quotes, name='quotes'),
	url(r'^qcallead/(?P<category>[0-9]+)/$', views.qcallead, name='qcallead'),
	#url(r'^qcalfun/(?P<category>[0-9]+)/$', views.qcalfun, name='qcalfun'),

]

