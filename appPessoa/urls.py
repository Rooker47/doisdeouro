from django.urls import path

from .views import PessoaInfo

urlpatterns = [
    path('', PessoaInfo.as_view(), name='infoPessoas'),

    path('pessoa_info', PessoaInfo.as_view(), name='infoPessoas'),

]
