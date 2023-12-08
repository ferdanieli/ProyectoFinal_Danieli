from django.contrib.auth.models import User
from django.db import models
import datetime
from blog.models import Carrera


class Comentarios(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
