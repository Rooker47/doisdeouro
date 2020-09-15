from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Entrada, Saida, Saldo


class AlmoxHome(TemplateView):
    template_name = "appAlmox/home.html"

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "ALMOXARIFADO"
        contexto['subtitulo1'] = "Entradas"
        contexto['subtitulo2'] = "Saídas"
        return contexto

# ================================================ SEÇÃO ENTRADA =======================================================
# CRIAR - ENTRADA ======================================================================================================
class EntradaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Entrada
    fields = ['nc', 'nomeMaterialEntrada', 'quantMaterialEntrada', 'data', 'nf', 'estoque_minimo']
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
    fields = ['nc', 'nomeMaterialEntrada', 'quantMaterialEntrada', 'data', 'nf', 'estoque_minimo']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('entradaList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar entrada de material"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - ENTRADA =====================================================================================================
class EntradaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u""
    model = Entrada
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
    template_name = 'appAlmox/listaEstoqueEntrada.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de entrada de material"
        return contexto

# ================================================ SEÇÃO SAIDA =========================================================
# CRIAR - SAIDA ========================================================================================================
class SaidaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saida
    fields = ['nc', 'nomeMaterialSaida', 'quantMaterialSaida', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('saidaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Nova saída de material"
        contexto['botao'] = "Registrar"
        return contexto


# ATUALIZAR - SAIDA ====================================================================================================
class SaidaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saida
    fields = ['nc', 'nomeMaterialSaida', 'quantMaterialSaida', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('saidaList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar saída de material"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - SAIDA =======================================================================================================
class SaidaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u""
    model = Saida
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('saidaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de saída de material"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - SAIDA =======================================================================================================
class SaidaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Saida
    template_name = 'appAlmox/listaEstoqueSaida.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de saída de material"
        return contexto


# ================================================ SEÇÃO SALDO =========================================================
# CRIAR - SALDO ========================================================================================================
class SaldoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saldo
    fields = ['nc', 'nomeMaterialSaida', 'quantMaterialSaida', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('saldoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Nova saída de material"
        contexto['botao'] = "Registrar"
        return contexto


# ATUALIZAR - SALDO ====================================================================================================
class SaldoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Almoxarifado"
    model = Saldo
    fields = ['nc', 'nomeMaterialSaida', 'quantMaterialSaida', 'data', 'destino', 'recebedor']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('saldoList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar saída de material"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - SALDO =======================================================================================================
class SaldoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u""
    model = Saldo
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('saldoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de saída de material"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - SALDO =======================================================================================================
class SaldoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Saldo
    template_name = 'appAlmox/listaEstoqueSaida.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de saída de material"
        return contexto
