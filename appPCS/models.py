from django.db import models
from appPrimeiraSecao.models import Pessoa
from django.utils import timezone


LOTACAO = [
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
    ('SSGG', 'Serviços Gerais'),
]

class Lotacao(models.Model):
    setor = models.CharField(max_length=100, choices=LOTACAO)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.setor, self.pessoa)
