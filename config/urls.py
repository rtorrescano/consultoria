from django.contrib import admin
from django.urls import path
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
]