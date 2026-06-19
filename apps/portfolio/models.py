from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion_corta = models.TextField()
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo