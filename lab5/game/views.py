from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .forms import *

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
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')


    else:
        form = AddNewsForm

    context = {
        'menu': menu,
        'form': form,
        'title': 'Add Page News',
    }
    return render(request, 'game/addpost.html', context=context)

def contact(request):
    return HttpResponse("FeedBack")

def show_post(request, post_slug):
    news = get_object_or_404(News, slug=post_slug);
    comment = len(Comment.objects.filter(news_id=news.news_id))
    return HttpResponse(f"Отображение статьи с id = {post_slug} {news.get_absolute_time()} {comment}" )

def show_category(request, post_slug):
    category = get_object_or_404(Category, slug=post_slug)
    news = News.objects.filter(category_id=category.category_id)
    cats = Category.objects.all()

    context = {
        'news': news,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': category.category_id,
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
