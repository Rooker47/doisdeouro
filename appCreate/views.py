from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao


class Create(TemplateView):
    template_name = "appCreate/index.html"

# CRIAR - PESSOA =======================================================================================================
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Pessoas"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - ARMA =========================================================================================================
class ArmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Armamento"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - REGISTRO RMB =================================================================================================
class RegistroRMBCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma', 'data']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('registroRMBList')

    def get_context_data(self, *args, **kwargs):
        contexto =  super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Registro na RMB"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - CONTATO ======================================================================================================
class ContatoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('contatoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Contato"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - ENDEREÇO =====================================================================================================
class EnderecoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('enderecoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Endereço"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - VIATURA ======================================================================================================
class ViaturaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis', 'status']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('viaturaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Viatura"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - GUARNIÇÕES ===================================================================================================
class GuarnicaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial', 'data']
    template_name = 'appCreate/form.html'
    success_url = reverse_lazy('guarnicaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Guarnição na Central de Operações"
        contexto['botao'] = "Cadastrar"
        return contexto
