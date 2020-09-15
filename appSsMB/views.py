from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Arma, RegistroRMB

class SsMBHome(TemplateView):
    template_name = "appSsMB/home.html"

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "RESERVA DE MATERIAL BÉLICO"
        contexto['subtitulo1'] = "Armas"
        contexto['subtitulo2'] = "Apetrechos"
        contexto['subtitulo3'] = "Registros"
        return contexto

# ================================================ SEÇÃO ARMA =======================================================
# CRIAR - ARMA ======================================================================================================
class ArmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"SsMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Nova cadastro de arma"
        contexto['botao'] = "Cadastrar"
        return contexto


# ATUALIZAR - ARMA ==================================================================================================
class ArmaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"SsMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('armaList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar cadastro de arma"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - ARMA =====================================================================================================
class ArmaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"SsMB"
    model = Arma
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar cadastro de arma"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - ARMA =====================================================================================================
class ArmaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Arma
    template_name = 'appSsMB/listaArmas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de armas cadastradas na RMB"
        return contexto

# ================================================ SEÇÃO RegistroRMB =========================================================
# CRIAR - SAIDA ========================================================================================================
class RegistroRMBCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('registroRMBList')

    def get_context_data(self, *args, **kwargs):
        contexto =  super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Registro na RMB"
        contexto['botao'] = "Cadastrar"
        return contexto

class RegistroRMBUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('registroRMBList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Registro da RMB"
        contexto['botao'] = "Atualizar"
        return contexto

class RegistroRMBDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    template_name = 'appDelete/form-excluir.html'
    success_url = reverse_lazy('registroRMBList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro na RMB"
        contexto['botao'] = "Deletar"
        return contexto

class RegistroRMBList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = RegistroRMB
    fields = ['policial', 'arma', 'data']
    template_name = 'appListas/listaRegistrosRMB.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Registro na RMB"
        return contexto
