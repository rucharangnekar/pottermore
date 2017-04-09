from django import forms
from django.contrib.auth.models import User

from .models import ForumDB, ThreadDB


class ForumDBForm(forms.ModelForm):

    class Meta:
        model = ForumDB
        fields = ['name', 'description']

    description = forms.CharField(widget=forms.Textarea(attrs={'cols':10 , 'rows':10, 'class' : 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 20, 'class': 'form-control'}))


class ThreadDBForm(forms.ModelForm):

    class Meta:
        model = ThreadDB
        fields = ['post']

    post = forms.CharField(widget=forms.Textarea(attrs={'size': 20, 'class': 'form-control'}))