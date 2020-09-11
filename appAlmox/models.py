from django.db import models
from appCreate.models import Pessoa
from django.utils import timezone

MOVIMENTO = [
    ('e', 'entrada'),
    ('s', 'saida'),
]
DESTINO = [
    ('P1', 'Primeira Seção'),
    ('P3', 'Terceira Seção'),
    ('P4', 'Quarta Seção'),
    ('Tes', 'Tesouraria'),
    ('Almox', 'Almoxarifado'),
    ('Almox', 'Almoxarifado'),
    ('Sec', 'Secretaria'),
    ('RMB', 'Material Bélico'),
    ('Transp', 'Seção de Transporte'),
    ('Com e TI', 'Seção de Comunicação e TI'),
    ('SsCOR', 'Correicional'),
]

class Entrada(models.Model):
    nc = models.PositiveIntegerField(primary_key=True, auto_created=True)
    nomeMaterialEntrada = models.CharField(max_length=100, verbose_name='Nome do material')
    quantMaterialEntrada = models.PositiveIntegerField(verbose_name='Quantidade do material')
    data = models.DateTimeField(default=timezone.now)
    nf = models.CharField(max_length=10, verbose_name='nota Fiscal', unique=True)
    estoque_minimo = models.PositiveIntegerField()


    def __str__(self):
        return '{} - {} - {}'.format(self.nomeMaterialEntrada, self.quantMaterialEntrada, self.estoque_minimo)


class Saida(models.Model):
    nc = models.PositiveIntegerField(primary_key=True, auto_created=True)
    nomeMaterialSaida = models.CharField(max_length=100, verbose_name='Nome do material')
    quantMaterialSaida = models.PositiveIntegerField(verbose_name='Quantidade do material')
    data = models.DateTimeField(default=timezone.now)
    destino = models.CharField(max_length=20, choices=DESTINO)
    recebedor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.material


class Saldo(models.Model):
    ncSaldo = models.PositiveIntegerField(primary_key=True, auto_created=True, editable=False)
    materialSaldo = models.CharField(max_length=100)
    quantSaldo = models.PositiveIntegerField(default=None)
    estoqueMinimoSaldo = models.PositiveIntegerField(default=None)

    def __str__(self):
        return '{} - {} - {}'.format(self.materialSaldo, self.estoqueSaldo, self.estoqueMinimoSaldo)
