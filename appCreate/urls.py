from django.urls import path


from .views import ViaturaCreate, GuarnicaoCreate


urlpatterns = [

    path('viaturas/', ViaturaCreate.as_view(), name='viaturaNew'),
    path('guarnicao/', GuarnicaoCreate.as_view(), name='guarnicaoNew'),
]