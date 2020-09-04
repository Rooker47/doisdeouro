from django.urls import path
from .views import Delete

from .views import PessoaDelete, ArmaDelete, RegistroRMBDelete, ContatoDelete, EnderecoDelete, ViaturaDelete, GuarnicaoDelete


urlpatterns = [
    path('', Delete.as_view(), name='apagar'),

    path('pessoas/<int:pk>', PessoaDelete.as_view(), name='pessoaDel'),
    path('armas/<int:pk>', ArmaDelete.as_view(), name='armaDel'),
    path('registrormb/<int:pk>', RegistroRMBDelete.as_view(), name='registroRMBDel'),
    path('contatos/<int:pk>', ContatoDelete.as_view(), name='contatoDel'),
    path('enderecos/<int:pk>', EnderecoDelete.as_view(), name='enderecoDel'),
    path('viaturas/<int:pk>', ViaturaDelete.as_view(), name='viaturaDel'),
    path('guarnicao/<int:pk>', GuarnicaoDelete.as_view(), name='guarnicaoDel'),
]