from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Pessoa, Contato, Endereco, Viatura, Guarnicao


class Create(TemplateView):
    template_name = "appCreate/home.html"

# CRIAR - PESSOA =======================================================================================================
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Pecúlio - Identificação"
        contexto['botao'] = "Cadastrar"
        return contexto




# CRIAR - REGISTRO RMB =================================================================================================



# CRIAR - CONTATO ======================================================================================================
class ContatoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('contatoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Pecúlio - Informações de Contato"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - ENDEREÇO =====================================================================================================
class EnderecoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('enderecoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Pecúlio - Endereços"
        contexto['botao'] = "Cadastrar"
        return contexto


# CRIAR - VIATURA ======================================================================================================
class ViaturaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis', 'status']
    template_name = 'appCore/form.html'
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
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('guarnicaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Guarnição na Central de Operações"
        contexto['botao'] = "Cadastrar"
        return contexto
