from django.db import models

class MensajeContacto(models.Model):
    TIPO_PROYECTO = [
        ('LP', 'Landing Page'),
        ('SW', 'Sitio Web'),
        ('SM', 'Sistema a Medida'),
        ('PM', 'Consultoría PM'),
        ('OT', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    tipo_proyecto = models.CharField(max_length=2, choices=TIPO_PROYECTO)
    presupuesto = models.CharField(max_length=50, blank=True)
    mensaje = models.TextField()
    fuente = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_proyecto}"