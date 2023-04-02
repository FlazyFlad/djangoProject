from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', cache_page(60)(GameHome.as_view()), name='home'),
    path('about/', GameAbout.as_view(), name='about'),
    path('addpost/', AddPage.as_view(), name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', GameDetail.as_view(), name='post'),
    path('search/', GameSearch.as_view(), name='search'),
    path('category/<slug:post_slug>/', cache_page(60)(GameCategory.as_view()), name='category'),
]

