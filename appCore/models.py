from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    criado = models.DateTimeField(verbose_name='criado em:',default=timezone.now)
    modificado = models.DateTimeField(verbose_name='modificado em:', default=timezone.now)

    class Meta:
        abstract = True
