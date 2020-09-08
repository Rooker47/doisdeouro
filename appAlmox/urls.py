from django.urls import path

from .views import Estoque

from .views import EntradaCreate, EntradaUpdate, EntradaDelete, EntradaList, SaidaCreate, SaidaUpdate, SaidaDelete, SaidaList, SaldoCreate, SaldoUpdate, SaldoDelete, SaldoList

urlpatterns = [
    path('entrada', Estoque.as_view(), name='entrada'),
    path('saida', Estoque.as_view(), name='saida'),
    path('saldo', Estoque.as_view(), name='saldo'),

    path('entrada/criar/', EntradaCreate.as_view(), name='entradaNew'),
    path('entrada/atualizar/<int:pk>', EntradaUpdate.as_view(), name='entradaUp'),
    path('entrada/deletar/<int:pk>', EntradaDelete.as_view(), name='entradaDel'),
    path('entrada/listar/', EntradaList.as_view(), name='entradaList'),

    path('saida/criar/', SaidaCreate.as_view(), name='saidaNew'),
    path('saida/atualizar/<int:pk>', SaidaUpdate.as_view(), name='saidaUp'),
    path('saida/deletar/<int:pk>', SaidaDelete.as_view(), name='saidaDel'),
    path('saida/listar/', SaidaList.as_view(), name='saidaList'),

    path('saldo/criar/', SaldoCreate.as_view(), name='saldoNew'),
    path('saldo/atualizar/<int:pk>', SaldoUpdate.as_view(), name='saldoUp'),
    path('saldo/deletar/<int:pk>', SaldoDelete.as_view(), name='saldoDel'),
    path('saldo/listar/', SaldoList.as_view(), name='saldoList'),
]