from django.db import models
from appCreate.models import Pessoa


class Entrada(models.Model):
    material = models.CharField(max_length=100)
    quant = models.IntegerField()
    data = models.DateTimeField()
    nf = models.CharField(max_length=10, verbose_name='nota Fiscal', unique=True)

    class Meta:
        ordering = 'material',

    def __str__(self):
        return self.material


class Saida(models.Model):
    material = models.CharField(max_length=100, unique=True)
    quant = models.IntegerField()
    data = models.DateTimeField()
    destino = models.CharField(max_length=20)
    recebedor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        ordering = 'material',
