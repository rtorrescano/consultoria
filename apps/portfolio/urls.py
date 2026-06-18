from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='portfolio'),
    path('<slug:slug>/', views.detalle, name='portfolio_detalle'),
]