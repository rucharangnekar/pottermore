
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404


def index(request):

    return render(request, 'hogwarts/start.html')

def why_to_reg(request):
    return render(request, 'hogwarts/why_to_reg.html')