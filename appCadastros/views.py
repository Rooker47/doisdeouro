from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao


class Cadastros(TemplateView):
    template_name = "appCadastros/form.html"

# ============================================= SEÇÃO CREATE ===========================================================
# CRIAR - PESSOA =======================================================================================================
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Pessoas"
        return contexto


# CRIAR - ARMA =========================================================================================================
class ArmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-armas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Armamento"
        return contexto


# CRIAR - REGISTRO RMB =================================================================================================
class RegistroRMBCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-registroRMB')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Registro na RMB"
        return contexto


# CRIAR - CONTATO ======================================================================================================
class ContatoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-contato')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Contato"
        return contexto


# CRIAR - ENDEREÇO =====================================================================================================
class EnderecoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-endereco')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Endereço"
        return contexto


# CRIAR - VIATURA ======================================================================================================
class ViaturaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-viatura')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Viatura"
        return contexto


# CRIAR - GUARNIÇÕES ===================================================================================================
class GuarnicaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Guarnição"
        return contexto


# ============================================= SEÇÃO UPDATE ===========================================================
# ATUALIZAR - PESSOA ===================================================================================================
class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Pessoas"
        return contexto


# ATUALIZAR - ARMA =====================================================================================================
class ArmaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-armas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Armamento"
        return contexto


# ATUALIZAR - REGISTRO RMB =============================================================================================
class RegistroRMBUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    fields = ['policial', 'arma']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-registroRMB')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Registro da RMB"
        return contexto


# ATUALIZAR - CONTATO ==================================================================================================
class ContatoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-contato')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Contato"
        return contexto


# ATUALIZAR - ENDEREÇO =================================================================================================
class EnderecoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-endereco')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Endereço"
        return contexto


# ATUALIZAR - VIATURA ==================================================================================================
class ViaturaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    fields = ['patrimonio', 'placa', 'chassis']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-viatura')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Viatura"
        return contexto


# ATUALIZAR - GUARNIÇÕES ===============================================================================================
class GuarnicaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Guarnição"
        return contexto


# ============================================= SEÇÃO DELETE ===========================================================
# DELETE - PESSOA ======================================================================================================
class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Pessoas"
        return contexto


# DELETE - ARMA ========================================================================================================
class ArmaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-armas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Armamento"
        return contexto


# DELETE - REGISTRO R===MB =============================================================================================
class RegistroRMBDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = RegistroRMB
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-registroRMB')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro na RMB"
        return contexto


# DELETE - CONTATO =====================================================================================================
class ContatoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Contato
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-contato')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Contato"
        return contexto


# DELETE - ENDEREÇO ====================================================================================================
class EnderecoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Endereco
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-endereco')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Endereço"
        return contexto


# DELETE - VIATURA =====================================================================================================
class ViaturaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-viatura')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Viatura"
        return contexto


# DELETE - GUARNIÇÕES=== ===============================================================================================
class GuarnicaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Guarnição"
        return contexto

#
# # ============================================= SEÇÃO LISTAR ===========================================================
# # LISTAR - ARMA ========================================================================================================
# class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"P1"
#     model = Pessoa
#     fields = ['graduacao', 'matricula', 'nome_guerra']
#     template_name = 'appCadastros/form.html'
#     success_url = reverse_lazy('listar-pessoas')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Pessoas"
#         return contexto
#
#
# # LISTAR - ARMA ========================================================================================================
# class ArmaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"RMB"
#     model = Arma
#     fields = ['especie', 'tipo', 'numero']
#     template_name = 'form.html'
#     success_url = reverse_lazy('listar-armas')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Armamento"
#         return contexto
#
#
# # LISTAR - REGISTRO RMB ================================================================================================
# class RegistroRMBList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"RMB"
#     model = RegistroRMB
#     fields = ['policial', 'arma']
#     template_name = 'form.html'
#     success_url = reverse_lazy('listar-registroRMB')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Registro da RMB"
#         return contexto
#
#
# # LISTAR - CONTATO =====================================================================================================
# class ContatoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"P1"
#     model = Contato
#     fields = ['idPessoaContato', 'tel1', 'tel2', 'email']
#     template_name = 'form.html'
#     success_url = reverse_lazy('listar-contato')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Contato"
#         return contexto
#
#
# # LISTAR - ENDEREÇO ====================================================================================================
# class EnderecoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"P1"
#     model = Endereco
#     fields = ['idPessoaEndereco', 'endereco', 'bairro', 'cidade', 'estado']
#     template_name = 'appCadastros/form.html'
#     success_url = reverse_lazy('listar-endereco')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Endereço"
#         return contexto
#
#
# # LISTAR - VIATURA =====================================================================================================
# class ViaturaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"STC"
#     model = Viatura
#     fields = ['patrimonio', 'placa', 'chassis']
#     template_name = 'appCadastros/form.html'
#     success_url = reverse_lazy('listar-viatura')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Viatura"
#         return contexto
#
#
# # LISTAR - GUARNIÇÕES ==================================================================================================
# class GuarnicaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"Central"
#     model = Guarnicao
#     fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
#     template_name = 'appCadastros/form.html'
#     success_url = reverse_lazy('listar-guarnicao')
#
#     def get_context_data(self, *args, **kwargs):
#         contexto = super().get_context_data(*args, **kwargs)
#         contexto['titulo'] = "Listar Guarnição"
#         return contexto
