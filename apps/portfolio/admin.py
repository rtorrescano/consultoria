from django.contrib import admin
from .models import Proyecto, Categoria, Tecnologia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono')

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'cliente', 'categoria', 'destacado', 'orden')
    list_filter = ('categoria', 'destacado')
    search_fields = ('titulo', 'cliente')
    filter_horizontal = ('tecnologias',)