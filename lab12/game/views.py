from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from .models import *
from .forms import *
from .utils import *

#Game Views
class GameHome(DataMixin, ListView):
    model = News
    template_name = 'game/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return context | c_def

    def get_queryset(self):
        return News.objects.annotate(count=Count('comment')).select_related('category_id')

class GameAbout(DataMixin, ListView):
    model = News
    template_name = 'game/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About")
        return context | c_def

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'game/addpost.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Page News")
        return context | c_def

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'game/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Contact")
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

class GameDetail(DataMixin, DetailView):
    model = News
    template_name = 'game/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(category_selected = context['news'].category_id)
        return context | c_def

class GameCategory(DataMixin, ListView):
    model = News
    template_name = 'game/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.annotate(count=Count('comment')).filter(category_id__slug=self.kwargs['post_slug']).select_related('category_id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['post_slug'])
        c_def = self.get_user_context(title='Category - ' + c.name,
                                      cat_selected = c.category_id,
                                      category_selected = c.name)
        return context | c_def

class GameSearch(DataMixin, ListView):
    model = News
    template_name = 'game/index.html'
    context_object_name = 'news'
    allow_empty = True

    def get_queryset(self):
        query = self.request.GET.get('q')
        if(query != " "):
            return News.objects.filter( Q(title__iregex=query) )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Search", q = self.request.GET.get('q'))
        return context | c_def

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'game/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'game/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')



#Api views

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        news = News.objects.filter(category_id=pk)
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def author(self, request, pk):
        news = News.objects.filter(author_id=pk)
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def recomends(self, request):
        news = News.objects.annotate(count=Count('comment')).order_by('-count')[0:3]
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


#Error def

def pageNotFound(request, exception):
    context = {
        'title': 'Error Page - 404',
        'error': '404'
    }
    return render(request, 'game/errorPage.html', context=context)

def pageNotAccess(request, *args, **argv):
    context = {
        'title': 'Error Page - 403',
        'error': '403'
    }
    return render(request, 'game/errorPage.html', context=context)

def pageBadRequest(request, *args, **argv):
    context = {
        'title': 'Error Page - 400',
        'error': '400'
    }
    return render(request, 'game/errorPage.html', context=context)

def internalServerError(request):
    context = {
        'title': 'Error Page - 500',
        'error': '500'
    }
    return render(request, 'game/errorPage.html', context=context)
