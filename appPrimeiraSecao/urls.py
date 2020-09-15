from django.urls import path

from .views import PimeiraSecaoHome
from .views import PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList, ContatoCreate, ContatoUpdate, ContatoDelete, ContatoList, EnderecoCreate, EnderecoUpdate, EnderecoDelete, EnderecoList

urlpatterns = [
    path('', PimeiraSecaoHome.as_view(), name='primeiraSecaoHome'),

    path('pessoa/criar/', PessoaCreate.as_view(), name='pessoaNew'),
    path('pessoa/atualizar/<int:pk>', PessoaUpdate.as_view(), name='pessoaUp'),
    path('pessoa/deletar/<int:pk>', PessoaDelete.as_view(), name='pessoaDel'),
    path('pessoa/listar/', PessoaList.as_view(), name='pessoaList'),

    path('contato/criar/', ContatoCreate.as_view(), name='contatoNew'),
    path('contato/atualizar/<int:pk>', ContatoUpdate.as_view(), name='contatoUp'),
    path('contato/deletar/<int:pk>', ContatoDelete.as_view(), name='contatoDel'),
    path('contato/listar/', ContatoList.as_view(), name='contatoList'),

    path('endereco/criar/', EnderecoCreate.as_view(), name='enderecoNew'),
    path('endereco/atualizar/<int:pk>', EnderecoUpdate.as_view(), name='enderecoUp'),
    path('endereco/deletar/<int:pk>', EnderecoDelete.as_view(), name='enderecoDel'),
    path('endereco/listar/', EnderecoList.as_view(), name='enderecoList'),
]