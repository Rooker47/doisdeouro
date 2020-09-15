from django.urls import path
from .views import Update

from .views import ViaturaUpdate, GuarnicaoUpdate


urlpatterns = [
    path('', Update.as_view()),


    path('viaturas/<int:pk>', ViaturaUpdate.as_view(), name='viaturaUp'),
    path('guarnicao/<int:pk>', GuarnicaoUpdate.as_view(), name='guarnicaoUp'),
]