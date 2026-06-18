from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nombre

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=30)
    icono = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    cliente = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tecnologias = models.ManyToManyField(Tecnologia)
    imagen_principal = models.ImageField(upload_to='proyectos/')
    descripcion_corta = models.TextField(max_length=200)
    descripcion_larga = models.TextField()
    reto = models.TextField()
    solucion = models.TextField()
    resultados = models.TextField(blank=True)
    url_sitio = models.URLField(blank=True)
    testimonio_cliente = models.TextField(blank=True)
    testimonio_nombre = models.CharField(max_length=80, blank=True)
    testimonio_cargo = models.CharField(max_length=80, blank=True)
    destacado = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo