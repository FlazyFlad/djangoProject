from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

menu = [{'title': "About", 'url_name': 'about'},
        {'title': 'Add News', 'url_name': 'add_post'},
        {'title': 'FeedBack', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
]

def index(request):
    news = News.objects.all()
    cats = Category.objects.all()

    context = {
        'news': news,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': 0,
    }
    return render(request, 'game/index.html', context=context)

def about(request):
    news = News.objects.all()

    context = {
        'news': news,
        'menu': menu,
        'title': 'About',
    }
    return render(request, 'game/about.html', context=context)

def login(request):
    return HttpResponse("Login")

def addpost(request):
    return HttpResponse("Add News")

def contact(request):
    return HttpResponse("FeedBack")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    cats = Category.objects.all()

    context = {
        'news': news,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': cat_id,
    }
    return render(request, 'game/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotAccess(request, *args, **argv):
    return HttpResponse('<h1>У страницы нет доступа</h1>')

def pageBadRequest(request, *args, **argv):
    return HttpResponse('<h1>Некоретный запрос</h1>')

def internalServerError(request):
    return HttpResponse('<h1>Нет доступа к серверу</h1>')
