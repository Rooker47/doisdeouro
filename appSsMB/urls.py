from django.urls import path

from .views import SsMBHome

from .views import ArmaCreate, ArmaUpdate, ArmaDelete, ArmaList, RegistroRMBCreate, RegistroRMBUpdate, RegistroRMBDelete, RegistroRMBList

urlpatterns = [
    path('', SsMBHome.as_view(), name='SsMBHome'),

    path('armas/criar/', ArmaCreate.as_view(), name='armaNew'),
    path('armas/atualizar/<int:pk>', ArmaUpdate.as_view(), name='armaUp'),
    path('armas/deletar/<int:pk>', ArmaDelete.as_view(), name='armaDel'),
    path('armas/listar/', ArmaList.as_view(), name='armaList'),

    path('registrormb/criar/', RegistroRMBCreate.as_view(), name='registroRMBNew'),
    path('registrormb/atualizar/<int:pk>', RegistroRMBUpdate.as_view(), name='registroRMBUp'),
    path('registrormb/deletar/<int:pk>', RegistroRMBDelete.as_view(), name='registroRMBDel'),
    path('registrormb/listar/', RegistroRMBList.as_view(), name='registroRMBList'),
]
