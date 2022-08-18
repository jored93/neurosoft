from django.urls import path
from app.consult import views

urlpatterns = [
    path('consult', views.consult, name='consult'),
]