from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from appCadastros.models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao

class Listas(TemplateView):
    template_name = "appListas/index.html"


# ============================================= SEÇÃO LISTAR ===========================================================
# LISTAR - PESSOA ========================================================================================================
class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    template_name = 'appListas/listaPessoas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Pessoas Cadastradas"
        return contexto


# LISTAR - ARMA ========================================================================================================
class ArmaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appListas/listaArmas.html'
    success_url = reverse_lazy('armaList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Armamento"
        return contexto


# LISTAR - REGISTRO RMB ================================================================================================
class RegistroRMBList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'appListas/listaRegistrosRMB.html'
    success_url = reverse_lazy('rmbList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Registro da RMB"
        return contexto


# LISTAR - CONTATO =====================================================================================================
class ContatoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appListas/listaContatos.html'
    success_url = reverse_lazy('contatoList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "contatoList"
        return contexto


# LISTAR - ENDEREÇO ====================================================================================================
class EnderecoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appListas/listaEnderecos.html'
    success_url = reverse_lazy('enderecoList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Endereços"
        return contexto


# LISTAR - VIATURA =====================================================================================================
class ViaturaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis']
    template_name = 'appListas/listaViaturas.html'
    success_url = reverse_lazy('viaturaList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Viaturas"
        return contexto


# LISTAR - GUARNIÇÕES ==================================================================================================
class GuarnicaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appListas/listaGuarnicao.html'
    success_url = reverse_lazy('guarnicaoList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista das Guarnições Cadastradas"
        return contexto
