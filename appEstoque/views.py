from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Entrada, Saida


class Estoque(TemplateView):
    template_name = "appEstoque/index.html"

# ================================================ SEÇÃO ENTRADA =======================================================
# CRIAR - ENTRADA ======================================================================================================
class EntradaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Entrada
    fields = ['material', 'quant', 'data', 'nf']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('entradaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Nova entrada de material"
        contexto['botao'] = "Registrar"
        return contexto


# ATUALIZAR - ENTRADA ==================================================================================================
class EntradaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Entrada
    fields = ['material', 'quant', 'data', 'nf']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('estoqueList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar entrada de material"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - ENTRADA =====================================================================================================
class EntradaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Entrada
    fields = ['material', 'quant', 'data', 'nf']
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('estoqueList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de entrada de material"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - ENTRADA =====================================================================================================
class EntradaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Entrada
    template_name = 'appEstoque/listaEstoque.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Pessoas Cadastradas"
        return contexto

# ================================================ SEÇÃO SAIDA =========================================================
# CRIAR - SAIDA ========================================================================================================
class SaidaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saida
    fields = ['material', 'quant', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('estoqueList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Nova entrada de material"
        contexto['botao'] = "Registrar"
        return contexto


# ATUALIZAR - SAIDA ====================================================================================================
class SaidaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saida
    fields = ['material', 'quant', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('estoqueList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar entrada de material"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - SAIDA =======================================================================================================
class SaidaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saida
    fields = ['material', 'quant', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('estoqueList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de entrada de material"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - SAIDA =======================================================================================================
class SaidaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Saida
    template_name = 'appEstoque/listaEstoque.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Pessoas Cadastradas"
        return contexto
