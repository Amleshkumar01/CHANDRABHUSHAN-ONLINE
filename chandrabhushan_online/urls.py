"""
URL configuration for CHANDRABHUSHAN ONLINE project.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin-django/', admin.site.urls),
    path('', include('shop.urls')),
]

# MEDIA FILES (Images upload fix - Render production)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# LOCAL DEVELOPMENT ONLY
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    