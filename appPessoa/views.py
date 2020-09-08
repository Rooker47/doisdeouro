from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import info_Pessoa


class PessoaInfo(TemplateView):
    template_name = "appPessoa/index.html"

# ================================================ SEÇÃO ENTRADA =======================================================
# INFO - PESSOA ======================================================================================================
class PessoaInfo(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = info_Pessoa
    fields = ['identificacao','contatos', 'endereco']
    template_name = 'appPessoa/pessoa_info.html'

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Dados pessoais de"
        contexto['botao'] = "Registrar"
        return contexto
