from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def lista(request):
    proyectos = Proyecto.objects.all().order_by('-destacado', 'orden')
    return render(request, 'portfolio/lista.html', {'proyectos': proyectos})

def detalle(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug)
    return render(request, 'portfolio/detalle.html', {'proyecto': proyecto})