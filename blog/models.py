from django.db import models
from django.contrib.auth.models import User
import datetime

class Carrera(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="carrera")
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    comision = models.IntegerField(unique=True)

    def __str__(self):
        return f" {self.titulo} - Comisión: {self.comision}"



