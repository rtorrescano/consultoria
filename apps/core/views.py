from django.shortcuts import render
from apps.portfolio.models import Proyecto
from apps.blog.models import Post

def home(request):
    context = {
        'proyectos': Proyecto.objects.filter(destacado=True)[:3],
        'posts': Post.objects.filter(publicado=True)[:3],
    }
    return render(request, 'home.html', context)