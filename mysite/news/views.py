from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic

from . models import NewsDB


def index(request):
    all_news = NewsDB.objects.all()
    context = {'all_news': all_news,
               }
    return render(request, 'news/index.html', context)


def detail(request, info_id):
    information = get_object_or_404(NewsDB, pk=info_id)
    information.count = int(information.count) + 1
    return render(request, 'news/detail.html', {'information': information})

