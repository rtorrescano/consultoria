from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publicado = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo