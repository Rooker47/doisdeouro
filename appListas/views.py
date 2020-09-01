from django.views.generic import TemplateView
from django.views.generic.list import ListView
from appCadastros.models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class Listas(TemplateView):
    template_name = "appListas/listaPessoas.html"


# ============================================= SEÇÃO LISTAR ===========================================================
# LISTAR - PESSOA ========================================================================================================
class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appListas/listaPessoas.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Pessoas"
        return contexto


# LISTAR - ARMA ========================================================================================================
class ArmaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Armamento"
        return contexto


# LISTAR - REGISTRO RMB ================================================================================================
class RegistroRMBList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'form.html'
    success_url = reverse_lazy('rmbList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Registro da RMB"
        return contexto


# LISTAR - CONTATO =====================================================================================================
class ContatoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-contato')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "contatoList"
        return contexto


# LISTAR - ENDEREÇO ====================================================================================================
class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-endereco')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "enderecoList"
        return contexto


# LISTAR - VIATURA =====================================================================================================
class ViaturaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-viatura')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "viaturaList"
        return contexto


# LISTAR - GUARNIÇÕES ==================================================================================================
class GuarnicaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "guarnicaoList"
        return contexto
