from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=30)#si es texto entoces se ponde CharField
    subtitulo = models.CharField(max_length=50) #mchar
    