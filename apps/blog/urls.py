from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='blog'),
    path('<slug:slug>/', views.detalle, name='blog_detalle'),
]