from django.contrib import admin
from .models import Etiqueta, Prenda, Outfit
from django.utils.html import format_html

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'enlace')
    search_fields = ('nombre',)

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('parte_arriba', 'pantalon', 'zapatos', 'etiqueta', 'mostrar_imagen', 'creador')
    search_fields = ('parte_arriba__nombre', 'pantalon__nombre', 'zapatos__nombre', 'creador__username')

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_imagen.short_description = 'Imagen'  # Título de la columna