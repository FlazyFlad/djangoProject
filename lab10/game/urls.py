from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', GameHome.as_view(), name='home'),
    path('about/', GameAbout.as_view(), name='about'),
    path('addpost/', AddPage.as_view(), name='add_post'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', GameDetail.as_view(), name='post'),
    path('search/', GameSearch.as_view(), name='search'),
    path('category/<slug:post_slug>/', GameCategory.as_view(), name='category'),

    path('api/v1/newslist', GameNewsApiView.as_view(), name='apiNews'),
    path('api/v1/newslist/<int:pk>/', GameNewsApiView.as_view(), name='apiNewsUpdate'),
    path('api/v1/categorylist', GameCategoryApiView.as_view() , name='apiCategory'),
    path('api/comment', GameCommentsApiView.as_view() , name='apiComment'),
]

