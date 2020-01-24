from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=30, unique=True)
    contraseña = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=70, unique=True)

