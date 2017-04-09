"""homepage URL Configuration
"""
from django.conf.urls import url
from . import views

app_name='homepage'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^base/$',views.base,name='base'),
	url(r'^register/$',views.about,name='register'),
	url(r'^getreg/$',views.getreg,name='reg'),
	url(r'^setreg/$', views.regi, name='regi'),
	#url(r'^forgot_user/$', views.forgot_user, name='forgot_user'),
	#url(r'^forgot_password/$', views.forgotpassword, name='forgotpassword'),
	url(r'^login/$',views.login_user,name='login'),
	url(r'^accounts/login/$', views.login_user, name='login'),

	url(r'^about/$', views.about, name='about'),
	url(r'^tnc/$', views.tnc, name='tnc'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^view_profile/$', views.view_profile, name='view_profile'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
	url(r'^activate/$',views.activatt,name='activatt'),
	url(r'^account_settings/$', views.account_settings, name='account_settings'),

]




