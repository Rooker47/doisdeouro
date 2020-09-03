from django.contrib.auth.models import User
from django.db import models
from appCore.models import Data
from appMaterial.models import Produto


MOVIMENTO = [
    ('e', 'entrada'),
    ('s', 'saida'),
]

class Estoque(Data):
    nf = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota Fiscal')
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-Criado'),

    def __str__(self):
        return str(self.pk)


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk'),

    def __str__(self):
        return '{} {} {}'.format(self.pk, self.estoque.pk, self.produto)
