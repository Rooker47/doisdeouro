from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from appCadastros.models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao


class Listas(TemplateView):
    template_name = "appListas/index.html"

# ============================================= SEÇÃO LISTAR ===========================================================
# LISTAR - PESSOA ========================================================================================================
class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pessoa
    template_name = 'appCadastros/listaPessoas.html'
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
    template_name = 'appCadastros/listaArmas.html'
    success_url = reverse_lazy('armaList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Armamento"
        return contexto


# LISTAR - REGISTRO RMB ================================================================================================
class RegistroRMBList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'appCadastros/listaRegistrosRMB.html'
    success_url = reverse_lazy('rmbList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Listar Registro da RMB"
        return contexto


# LISTAR - CONTATO =====================================================================================================
class ContatoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appCadastros/listaContatos.html'
    success_url = reverse_lazy('contatoList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "contatoList"
        return contexto


# LISTAR - ENDEREÇO ====================================================================================================
class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCadastros/listaEnderecos.html'
    success_url = reverse_lazy('enderecoList')
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
    template_name = 'appCadastros/listaViaturas.html'
    success_url = reverse_lazy('viaturaList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Viaturas"
        return contexto


# LISTAR - GUARNIÇÕES ==================================================================================================
class GuarnicaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCadastros/listaGuarnicao.html'
    success_url = reverse_lazy('guarnicaoList')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista das Guarnições Cadastradas"
        return contexto
