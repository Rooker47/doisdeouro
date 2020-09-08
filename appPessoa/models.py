from django.db import models
from appCreate.models import Pessoa, Contato, Endereco

# INFO - PESSOA ========================================================================================================
class info_Pessoa(models.Model):
    identificacao = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    contatos = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
