from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

def index(request):
    news = News.objects.all()
    return render(request, 'game/index.html', {'news': news, 'title': 'Главная страница'})

def about(request):
    return render(request, 'game/about.html', {'title': 'О странице'})

def register(request):
    return render(request, 'game/register.html')

def login(request):
    return render(request, 'game/login.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotAccess(request, *args, **argv):
    return HttpResponse('<h1>У страницы нет доступа</h1>')

def pageBadRequest(request, *args, **argv):
    return HttpResponse('<h1>Некоретный запрос</h1>')

# def internalServerError(request):
#     return HttpResponse('<h1>Нет доступа к серверу</h1>')
