from django.shortcuts import render, get_object_or_404
from news.models import New, NewCategory, Author
from django.core.paginator import Paginator


# Create your views here.
def index(request):

    contex = {
        'title': 'Главная',
        'categories': NewCategory.objects.all(),
        'news': New.objects.all()
    }
    return render(request, 'news/index.html', contex)


def new_detail(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    contex = {
        'title': 'All news',
        'author': author,
        'new': new,

    }
    return render(request, 'news/new_detail.html', contex)


def news(request, page=1):
    news = New.objects.all()
    contex = {
        'title': 'Новости',
        'categories': NewCategory.objects.all(),
        'news': news
    }
    paginator = Paginator(news, 9)
    news_paginator = paginator.page(page)
    contex.update({'news': news_paginator})
    return render(request, 'news/new.html', contex)


def author(request):
    contex = {
        'title': 'All Authors',
        'authors': Author.objects.all()
    }
    return render(request, 'news/author.html', contex)
