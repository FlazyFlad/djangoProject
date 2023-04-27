from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from game.views import *
from gamesite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('capthca,', include('captcha.urls')),
    path('', include('game.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

handler404 = pageNotFound
handler403 = pageNotAccess
handler400 = pageBadRequest
handler500 = internalServerError

