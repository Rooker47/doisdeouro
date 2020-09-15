from django.urls import path
from .views import Listas

from .views import ViaturaList, GuarnicaoList


urlpatterns = [
    path('', Listas.as_view(), name='listar'),


    path('viaturas/', ViaturaList.as_view(), name='viaturaList'),
    path('guarnicao/', GuarnicaoList.as_view(), name='guarnicaoList'),
]
