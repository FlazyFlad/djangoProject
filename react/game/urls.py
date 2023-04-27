from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'comment', CommentViewSet)
print(router.urls)

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

    path('api/v1/', include(router.urls), name='apiNews'),
]

