from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nomeCompletoUsuario = models.CharField(max_length=100, null=True)
    matriculaUsuario = models.IntegerField(null=True)
    telefoneUsuario = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
