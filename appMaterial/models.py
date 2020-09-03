from django.db import models

class Produto(models.Model):
    produto = models.CharField(max_length=100, unique=True)
    estoque = models.IntegerField(verbose_name='estoque atual')
    estoque_minimo = models.PositiveIntegerField(default=0, verbose_name='estoque mínimo')

    class Meta:
        ordering = ('produto'),

    def __str__(self):
        return self.produto
