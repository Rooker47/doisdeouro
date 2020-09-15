from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Pessoa, Contato, Endereco

#==================================================== HOME =============================================================
class PimeiraSecaoHome(TemplateView):
    template_name = "appPrimeiraSecao/home.html"

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "PRIMEIRA SEÇÃO"
        contexto['subtitulo1'] = "Cadastrar pessoas"
        contexto['subtitulo2'] = "Cadastrar contatos"
        contexto['subtitulo3'] = "Cadastrar endereços"
        return contexto


#================================================== SEÇÃO PESSOA =======================================================
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

# ATUALIZAR - PESSOA ===================================================================================================
class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('pessoaList')


    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Pessoas"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - PESSOA =====================================================================================================
class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    template_name = 'appCore/form-excluir.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Pessoa"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - PESSOA ========================================================================================================
class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Pessoa
    template_name = 'appPrimeiraSecao/listaPessoas.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Pessoas Cadastradas"
        return contexto

#================================================== SEÇÃO CONTATO ======================================================
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


# ATUALIZAR - CONTATO ==================================================================================================
class ContatoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('contatoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Contato"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - CONTATO =====================================================================================================
class ContatoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    template_name = 'appDelete/form-excluir.html'
    success_url = reverse_lazy('contatoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Contato"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - CONTATO =====================================================================================================
class ContatoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appPrimeiraSecao/listaContatos.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de contatos cadastrados"
        return contexto


#================================================== SEÇÃO ENDEREÇO =====================================================
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


# ATUALIZAR - ENDEREÇO =================================================================================================
class EnderecoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('enderecoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Endereço"
        contexto['botao'] = "Atualizar"
        return contexto


# DELETE - ENDEREÇO ====================================================================================================
class EnderecoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    template_name = 'appDelete/form-excluir.html'
    success_url = reverse_lazy('enderecoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Endereço"
        contexto['botao'] = "Deletar"
        return contexto


# LISTAR - ENDEREÇO ====================================================================================================
class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appPrimeiraSecao/listaEnderecos.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Lista de Endereços"
        return contexto
