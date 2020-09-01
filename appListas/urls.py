from django.urls import path
from .views import Listas
from .views import PessoaList, ArmaList, RegistroRMBList, ContatoList, EnderecoList, ViaturaList, GuarnicaoList


urlpatterns = [
    path('', Listas.as_view(), name='listar'),

    path('pessoas/', PessoaList.as_view(), name='pessoaList'),
    path('armas/', ArmaList.as_view(), name='armaList'),
    path('registrormb/', RegistroRMBList.as_view(), name='rmbList'),
    path('contatos/', ContatoList.as_view(), name='contatoList'),
    path('enderecos/', EnderecoList.as_view(), name='enderecoList'),
    path('viaturas/', ViaturaList.as_view(), name='viaturaList'),
    path('guarnicao/', GuarnicaoList.as_view(), name='guarnicaoList'),
]