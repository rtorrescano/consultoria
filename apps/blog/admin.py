from django.contrib import admin
from .models import Post, CategoriaBlog

@admin.register(CategoriaBlog)
class CategoriaBlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'categoria', 'publicado', 'fecha_publicacion')
    list_filter = ('publicado', 'categoria')
    search_fields = ('titulo', 'contenido')