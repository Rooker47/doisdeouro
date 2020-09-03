from django.db import models

class Data(models.Model):
    Criado = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='registrado em')
    Modificado = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='modificado em')

    class Meta:
        abstract = True
