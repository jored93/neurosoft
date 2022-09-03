from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

contentPath = "neutrosoft"
env = "/dev/"
url = contentPath + env

urlpatterns = [
    path('admin/', admin.site.urls),
    path(url, include('app.consult.router')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)