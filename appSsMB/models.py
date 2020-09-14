from django.db import models
from appCreate.models import Pessoa
from django.utils import timezone

ARMA_ESPECIE = [
    ('Arma de fogo', 'Arma de fogo'),
    ('Colete', 'Colete'),
]

ARMA_TIPO = [
    ('Revr', 'Revólver'),
    ('Pst', 'Pistola'),
    ('Smtr', 'Submetralhadora'),
    ('Fz', 'Fuzil'),
]


class Arma(models.Model):
    especie = models.CharField(max_length=15, choices=ARMA_ESPECIE)
    tipo = models.CharField(max_length=15, choices=ARMA_TIPO)
    numero = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return "{} {}".format(self.tipo, self.numero)


class RegistroRMB(models.Model):
    policial = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="identificação")
    arma = models.OneToOneField(Arma, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now, auto_now=False, verbose_name="registro em")

    def __str__(self):
        return "{} {}".format(self.policial, self.arma)
