from django.urls import path

from .views import PCSHome

from .views import LotacaoCreate, LotacaoUpdate, LotacaoDelete, LotacaoList

urlpatterns = [
    path('', PCSHome.as_view(), name='pcsHome'),

    path('lotacao/criar/', LotacaoCreate.as_view(), name='lotacaoNew'),
    path('lotacao/atualizar/<int:pk>', LotacaoUpdate.as_view(), name='lotacaoUp'),
    path('lotacao/deletar/<int:pk>', LotacaoDelete.as_view(), name='lotacaoDel'),
    path('lotacao/listar/', LotacaoList.as_view(), name='lotacaoList'),
]
