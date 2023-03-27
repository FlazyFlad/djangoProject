from django.urls import path

from .views import *


urlpatterns = [
    path('', GameHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpost/', AddPage.as_view(), name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', GameDetail.as_view(), name='post'),
    path('category/<slug:post_slug>/', GameCategory.as_view(), name='category'),
]

