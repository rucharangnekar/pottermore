from django.conf.urls import url
from . import views

app_name = 'hogwarts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^why_to_reg/$', views.why_to_reg, name='why_to_reg'),

]
