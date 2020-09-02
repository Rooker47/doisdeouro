from django.urls import path
from .views import Cadastros

from .views import PessoaCreate, ArmaCreate, RegistroRMBCreate, ContatoCreate, EnderecoCreate, ViaturaCreate, GuarnicaoCreate
from .views import PessoaUpdate, ArmaUpdate, RegistroRMBUpdate, ContatoUpdate, EnderecoUpdate, ViaturaUpdate, GuarnicaoUpdate
from .views import PessoaDelete, ArmaDelete, RegistroRMBDelete, ContatoDelete, EnderecoDelete, ViaturaDelete, GuarnicaoDelete


urlpatterns = [
    path('', Cadastros.as_view(), name='cadastrar'),

    path('pessoa/', PessoaCreate.as_view(), name='pessoaNew'),
    path('arma/', ArmaCreate.as_view(), name='armaNew'),
    path('registrormb/', RegistroRMBCreate.as_view(), name='rmbNew'),
    path('contato/', ContatoCreate.as_view(), name='contatoNew'),
    path('endereco/', EnderecoCreate.as_view(), name='enderecoNew'),
    path('viatura/', ViaturaCreate.as_view(), name='viaturaNew'),
    path('guarnicao/', GuarnicaoCreate.as_view(), name='guarnicaoNew'),

    path('editar/pessoa/<int:pk>', PessoaUpdate.as_view(), name='pessoaUp'),
    path('editar/arma/<int:pk>', ArmaUpdate.as_view(), name='armaUp'),
    path('editar/rmb/<int:pk>', RegistroRMBUpdate.as_view(), name='rmbUp'),
    path('editar/contato/<int:pk>', ContatoUpdate.as_view(), name='contatoUp'),
    path('editar/endereco/<int:pk>', EnderecoUpdate.as_view(), name='enderecoUp'),
    path('editar/viatura/<int:pk>', ViaturaUpdate.as_view(), name='viaturaUp'),
    path('editar/centralvtr/<int:pk>', GuarnicaoUpdate.as_view(), name='guarnicaoUp'),

    path('excluir/pessoa/<int:pk>', PessoaDelete.as_view(), name='pessoaDel'),
    path('excluir/arma/<int:pk>', ArmaDelete.as_view(), name='armaDel'),
    path('excluir/rmb/<int:pk>', RegistroRMBDelete.as_view(), name='rmbDel'),
    path('excluir/contato/<int:pk>', ContatoDelete.as_view(), name='contatoDel'),
    path('excluir/endereco/<int:pk>', EnderecoDelete.as_view(), name='enderecoDel'),
    path('excluir/viatura/<int:pk>', ViaturaDelete.as_view(), name='viaturaDel'),
    path('excluir/centralvtr/<int:pk>', GuarnicaoDelete.as_view(), name='guarnicaoDel'),

]