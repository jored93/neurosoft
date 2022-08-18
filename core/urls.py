from django.contrib import admin
from django.urls import path, include

contentPath = "neutrosoft"
env = "/dev/"
url = contentPath + env

urlpatterns = [
    path('admin/', admin.site.urls),
    path(url, include('app.consult.urls')),
]
