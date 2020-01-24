from django.db import models
from Apps.Login import models as models_login
from django.contrib.auth.models import User as models_user

# Create your models here.

class Categorias(models.Model):
    usuario = models.ForeignKey(models_user, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)

class Notes(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    usuario = models.ForeignKey(models_user, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categorias',on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    fecha = models.DateField(auto_now_add=True)