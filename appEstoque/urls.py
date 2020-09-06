from django.urls import path

from .views import Estoque

from .views import EntradaCreate, EntradaUpdate, EntradaDelete, EntradaList, SaidaCreate, SaidaUpdate, SaidaDelete, SaidaList


urlpatterns = [
    path('', Estoque.as_view(), name='estoque'),

    path('entrada/criar/', EntradaCreate.as_view(), name='entradaNew'),
    path('entrada/atualizar/<int:pk>', EntradaUpdate.as_view(), name='entradaUp'),
    path('entrada/deletar/<int:pk>', EntradaDelete.as_view(), name='entradaDel'),
    path('entrada/listar/', EntradaList.as_view(), name='entradaList'),
    path('saida/criar/', SaidaCreate.as_view(), name='saidaNew'),
    path('saida/atualizar/<int:pk>', SaidaUpdate.as_view(), name='saidaUp'),
    path('saida/deletar/<int:pk>', SaidaDelete.as_view(), name='saidaDel'),
    path('saida/listar/', SaidaList.as_view(), name='saidaList'),
]