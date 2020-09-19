from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    email = models.EmailField()

class Perfil(models.Model):
    nomeCompletoUsuario = models.CharField(max_length=100, null=True, verbose_name="nome completo")
    matriculaUsuario = models.IntegerField(null=True, verbose_name="matrícula")
    telefoneUsuario = models.CharField(max_length=16, null=True, verbose_name="telefone")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="nome de usuário")

    def __str__(self):
        return "{}".format(self.usuario)
