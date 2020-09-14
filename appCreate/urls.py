from django.urls import path
from .views import Create

from .views import PessoaCreate, ContatoCreate, EnderecoCreate, ViaturaCreate, GuarnicaoCreate


urlpatterns = [
    path('', Create.as_view(), name='novo'),

    path('pessoa/', PessoaCreate.as_view(), name='pessoaNew'),
    path('contatos/', ContatoCreate.as_view(), name='contatoNew'),
    path('enderecos/', EnderecoCreate.as_view(), name='enderecoNew'),
    path('viaturas/', ViaturaCreate.as_view(), name='viaturaNew'),
    path('guarnicao/', GuarnicaoCreate.as_view(), name='guarnicaoNew'),
]