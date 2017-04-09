from django.contrib.auth.models import User
from django import forms
from . models import Myusr, Profile


class uform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'cpassword']


class EditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic']

class chform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password', 'cpassword']


