from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from appCreate.models import Pessoa, Arma, Contato, Endereco, Viatura, Guarnicao


class Listas(TemplateView):
    template_name = "appListas/home.html"

# LISTAR - PESSOA ========================================================================================================
class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Pessoa
    template_name = 'appPessoa/listaPessoas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Pessoas Cadastradas"
        return contexto


# LISTAR - ARMA ========================================================================================================
class ArmaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appListas/listaArmas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Armamento"
        return contexto


# LISTAR - REGISTRO RMB ================================================================================================



# LISTAR - CONTATO =====================================================================================================
class ContatoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appListas/listaContatos.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de contatos cadastrados"
        return contexto


# LISTAR - ENDEREÇO ====================================================================================================
class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appListas/listaEnderecos.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Endereços"
        return contexto


# LISTAR - VIATURA =====================================================================================================
class ViaturaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis']
    template_name = 'appListas/listaViaturas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Viaturas"
        return contexto


# LISTAR - GUARNIÇÕES ==================================================================================================
class GuarnicaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial', 'data']
    template_name = 'appListas/listaGuarnicao.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista das Guarnições Cadastradas"
        return contexto
