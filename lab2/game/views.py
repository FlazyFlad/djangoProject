from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index(request):
    return HttpResponse("<h2>Главная страница сайта</h2>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotAccess(request, *args, **argv):
    return HttpResponse('<h1>У страницы нет доступа</h1>')

def pageBadRequest(request, *args, **argv):
    return HttpResponse('<h1>Некоретный запрос</h1>')

def internalServerError(request):
    return HttpResponse('<h1>Нет доступа к серверу</h1>')
