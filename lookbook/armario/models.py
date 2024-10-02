from django.db import models
from django.contrib.auth.models import User


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, choices=[('verano', 'Verano'), ('invierno', 'Invierno')])

    def __str__(self):
        return self.nombre


class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    enlace = models.URLField(blank=True, null=True)  # Enlace a más detalles sobre la prenda

    def __str__(self):
        return self.nombre


class Outfit(models.Model):
    parte_arriba = models.ForeignKey(Prenda, related_name='parte_arriba', on_delete=models.CASCADE)
    pantalon = models.ForeignKey(Prenda, related_name='pantalon', on_delete=models.CASCADE)
    zapatos = models.ForeignKey(Prenda, related_name='zapatos', on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='outfits/', blank=False, null=False)  # Imagen obligatoria
    creador = models.ForeignKey(User, on_delete=models.CASCADE)  # Campo para el creador del outfit

    def __str__(self):
        return f"Outfit: {self.parte_arriba}, {self.pantalon}, {self.zapatos} (Creador: {self.creador.username})"

