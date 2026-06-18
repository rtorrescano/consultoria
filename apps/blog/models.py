from django.db import models

class CategoriaBlog(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    extracto = models.TextField(max_length=300)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/', blank=True)
    categoria = models.ForeignKey(CategoriaBlog, on_delete=models.PROTECT)
    autor = models.CharField(max_length=80, default="Raúl Torrescano")
    publicado = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo