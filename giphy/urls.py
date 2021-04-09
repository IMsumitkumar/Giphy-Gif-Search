
from django.contrib import admin
from django.urls import path
from app.views import home, trending_sticker
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('trending-sticker/', trending_sticker, name='trending_sticker')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)