from django.shortcuts import render, get_object_or_404
from .models import Post

def lista(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista.html', {'posts': posts})

def detalle(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'blog/detalle.html', {'post': post})