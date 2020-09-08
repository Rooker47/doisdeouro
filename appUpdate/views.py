from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from appCreate.models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao

class Update(TemplateView):
    template_name = "appUpdate/index.html"

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


# ATUALIZAR - ARMA =====================================================================================================
class ArmaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Armamento"
        contexto['botao'] = "Atualizar"
        return contexto


# ATUALIZAR - REGISTRO RMB =============================================================================================
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


# ATUALIZAR - VIATURA ==================================================================================================
class ViaturaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis', 'status']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('viaturaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Viatura"
        contexto['botao'] = "Atualizar"
        return contexto


# ATUALIZAR - GUARNIÇÕES ===============================================================================================
class GuarnicaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCore/form.html'
    success_url = reverse_lazy('guarnicaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Guarnição"
        contexto['botao'] = "Atualizar"
        return contexto
