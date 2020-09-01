from django.urls import path

from .views import Listas
from .views import PessoaList, ArmaList, RegistroRMBList, ContatoList, EnderecoList, ViaturaList, GuarnicaoList

urlpatterns = [
    path('', Listas.as_view(), name='listar'),

    path('pessoa/', PessoaList.as_view(), name='pessoaList'),
    path('arma/', ArmaList.as_view(), name='armaList'),
    path('rmb/', RegistroRMBList.as_view(), name='rmbList'),
    path('contato/', ContatoList.as_view(), name='contatoList'),
    path('endereco/', EnderecoList.as_view(), name='enderecoList'),
    path('viatura/', ViaturaList.as_view(), name='viaturaList'),
    path('guarnicao/', GuarnicaoList.as_view(), name='guarnicaoList'),
]
