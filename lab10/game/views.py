from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

from .models import *
from django.contrib.auth.models import User
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

class GameNewsApiView(APIView):
    def get(self, request):
        news = News.objects.all()
        return Response({'posts': NewsSerializer(news, many=True).data})

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = News.objects.get(news_id=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        news = News.objects.get(news_id=pk)
        news.delete()

        return Response({"post": "Delete post " + str(pk)})

class GameCategoryApiView(generics.ListAPIView):
    def get(self, request):
        category = Category.objects.all()
        return Response({'category': CategorySerializer(category, many=True).data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'category': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Category.objects.get(news_id=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"category": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        category = Category.objects.get(news_id=pk)
        category.delete()

        return Response({"category": "Delete post " + str(pk)})

class GameCommentsApiView(generics.ListAPIView):

    def get(self, request):
        comment = Comment.objects.get()
        return Response({'comments': CommentsSerializer(comment, many=True).data})

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'comments': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Category.objects.get(news_id=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CommentsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"comments": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        category = Category.objects.get(news_id=pk)
        category.delete()

        return Response({"comments": "Delete post " + str(pk)})

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
