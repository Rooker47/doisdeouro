from django.urls import path
from .views import Delete

from .views import ViaturaDelete, GuarnicaoDelete


urlpatterns = [
    path('', Delete.as_view(), name='apagar'),


    path('viaturas/<int:pk>', ViaturaDelete.as_view(), name='viaturaDel'),
    path('guarnicao/<int:pk>', GuarnicaoDelete.as_view(), name='guarnicaoDel'),
]