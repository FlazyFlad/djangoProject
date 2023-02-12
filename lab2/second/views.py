from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return  HttpResponse("Страница нашего приложения second.")

def categories(request, cat):
    return HttpResponse(f"<h1>Статья по категориям</h1><p>{cat}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotAccess(request, *args, **argv):
    return HttpResponse('<h1>У страницы нет доступа</h1>')

def pageBadRequest(request, *args, **argv):
    return HttpResponse('<h1>Некоретный запрос</h1>')

def internalServerError(request):
    return HttpResponse('<h1>Нет доступа к серверу</h1>')