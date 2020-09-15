from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Lotacao


class PCSHome(TemplateView):
    template_name = "appPCS/home.html"

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "PCS"
        contexto['subtitulo1'] = "Lotação"
        return contexto

# ================================================ SEÇÃO ENTRADA =======================================================
# CRIAR - ENTRADA ======================================================================================================
class LotacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"PCS"
    model = Lotacao
    fields = ['setor', 'pessoa']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('lotacaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lotar Policial"
        contexto['botao'] = "Lotar"
        return contexto


# ATUALIZAR - ENTRADA ==================================================================================================
class LotacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"PCS"
    model = Lotacao
    fields = ['setor', 'pessoa']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('lotacaoList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar lotação"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - ENTRADA =====================================================================================================
class LotacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u""
    model = Lotacao
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('lotacaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de lotação"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - ENTRADA =====================================================================================================
class LotacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Lotacao
    template_name = 'appPCS/listaLotacao.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista das Seções e seus efetivos"
        return contexto
