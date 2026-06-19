from django.shortcuts import render
from apps.portfolio.models import Proyecto
from apps.blog.models import Post

def home(request):
    context = {
        'proyectos': Proyecto.objects.filter(destacado=True)[:3],
        'posts': Post.objects.filter(publicado=True)[:3],
    }
    return render(request, 'home.html', context)

def servicios(request):
    return render(request, 'servicios.html')

def portafolio(request):
    context = {
        'proyectos': Proyecto.objects.all(),
    }
    return render(request, 'portafolio.html', context)

def sobre_mi(request):
    return render(request, 'sobre-mi.html')

def blog(request):
    context = {
        'posts': Post.objects.filter(publicado=True),
    }
    return render(request, 'blog.html', context)

def contacto(request):
    return render(request, 'contacto.html')