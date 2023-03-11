from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

menu = [{'title': "About", 'url_name': 'about'},
        {'title': 'Add News', 'url_name': 'add_post'},
        {'title': 'FeedBack', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
]

# def index(request):
#     news = News.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'news': news,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': 0,
#     }
#     return render(request, 'game/index.html', context=context)

class GameHome(ListView):
    model = News
    template_name = 'game/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        context['cats'] = Category.objects.all()
        return context

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

class AddPage(CreateView):
    form_class = AddNewsForm
    template_name = 'game/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add Page News'
        return context

# def addpost(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddNewsForm
#
#     context = {
#         'menu': menu,
#         'form': form,
#         'title': 'Add Page News',
#     }
#     return render(request, 'game/addpost.html', context=context)

def contact(request):
    return HttpResponse("FeedBack")

class GameDetail(DetailView):
    model = News
    template_name = 'game/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Post'
        return context

# def show_post(request, post_slug):
#     news = get_object_or_404(News, slug=post_slug);
#     comment = len(Comment.objects.filter(news_id=news.news_id))
#     return HttpResponse(f"Отображение статьи с id = {post_slug} {news.get_absolute_time()} {comment}" )

class GameCategory(ListView):
    model = News
    template_name = 'game/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id__slug=self.kwargs['post_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['news'][0].category_id)
        context['cat_selected'] = context['news'][0].category_id_id
        context['category_selected'] = context['news'][0].category_id
        context['cats'] = Category.objects.all()
        return context

# def show_category(request, post_slug):
#     category = get_object_or_404(Category, slug=post_slug)
#     news = News.objects.filter(category_id=category.category_id)
#     cats = Category.objects.all()
#
#     context = {
#         'news': news,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Main Page',
#         'category_selected': category,
#         'cat_selected': category.category_id,
#     }
#     return render(request, 'game/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotAccess(request, *args, **argv):
    return HttpResponse('<h1>У страницы нет доступа</h1>')

def pageBadRequest(request, *args, **argv):
    return HttpResponse('<h1>Некоретный запрос</h1>')

def internalServerError(request):
    return HttpResponse('<h1>Нет доступа к серверу</h1>')
