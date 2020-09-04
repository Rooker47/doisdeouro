from django.urls import path
from .views import Create

from .views import PessoaCreate, ArmaCreate, RegistroRMBCreate, ContatoCreate, EnderecoCreate, ViaturaCreate, GuarnicaoCreate


urlpatterns = [
    path('', Create.as_view(), name='novo'),

    path('pessoa/', PessoaCreate.as_view(), name='pessoaNew'),
    path('armas/', ArmaCreate.as_view(), name='armaNew'),
    path('registrormb/', RegistroRMBCreate.as_view(), name='registroRMBNew'),
    path('contatos/', ContatoCreate.as_view(), name='contatoNew'),
    path('enderecos/', EnderecoCreate.as_view(), name='enderecoNew'),
    path('viaturas/', ViaturaCreate.as_view(), name='viaturaNew'),
    path('guarnicao/', GuarnicaoCreate.as_view(), name='guarnicaoNew'),
]