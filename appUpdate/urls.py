from django.urls import path
from .views import Update

from .views import PessoaUpdate, ArmaUpdate, RegistroRMBUpdate, ContatoUpdate, EnderecoUpdate, ViaturaUpdate, GuarnicaoUpdate


urlpatterns = [
    path('', Update.as_view()),

    path('pessoas/<int:pk>', PessoaUpdate.as_view(), name='pessoaUp'),
    path('armas/<int:pk>', ArmaUpdate.as_view(), name='armaUp'),
    path('registrormb/<int:pk>', RegistroRMBUpdate.as_view(), name='registroRMBUp'),
    path('contatos/<int:pk>', ContatoUpdate.as_view(), name='contatoUp'),
    path('enderecos/<int:pk>', EnderecoUpdate.as_view(), name='enderecoUp'),
    path('viaturas/<int:pk>', ViaturaUpdate.as_view(), name='viaturaUp'),
    path('guarnicao/<int:pk>', GuarnicaoUpdate.as_view(), name='guarnicaoUp'),
]