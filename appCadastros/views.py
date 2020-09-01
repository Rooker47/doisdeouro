from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao


class Cadastros(TemplateView):
    template_name = "appCadastros/form.html"

# ============================================= SEÇÃO CREATE ===========================================================
# CRIAR - PESSOA =======================================================================================================
class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Pessoas"
        return contexto


# CRIAR - ARMA =========================================================================================================
class ArmaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Armamento"
        return contexto


# CRIAR - REGISTRO RMB =================================================================================================
class RegistroRMBCreate(LoginRequiredMixin, CreateView):
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
class ContatoCreate(LoginRequiredMixin, CreateView):
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
class EnderecoCreate(LoginRequiredMixin, CreateView):
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
class ViaturaCreate(LoginRequiredMixin, CreateView):
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
class GuarnicaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    fields = ['vtrPrefixo', 'vtr', 'condutor', 'kmInicial']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Cadastrar Guarnição na Central de Operações"
        return contexto


# ============================================= SEÇÃO UPDATE ===========================================================
# ATUALIZAR - PESSOA ===================================================================================================
class PessoaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    fields = ['graduacao', 'matricula', 'nome_guerra']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('pessoaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Pessoas"
        return contexto


# ATUALIZAR - ARMA =====================================================================================================
class ArmaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"RMB"
    model = Arma
    fields = ['especie', 'tipo', 'numero']
    template_name = 'appCadastros/form.html'
    success_url = reverse_lazy('armaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Atualizar Armamento"
        return contexto


# ATUALIZAR - REGISTRO RMB =============================================================================================
class RegistroRMBUpdate(LoginRequiredMixin, UpdateView):
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
class ContatoUpdate(LoginRequiredMixin, UpdateView):
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
class EnderecoUpdate(LoginRequiredMixin, UpdateView):
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
class ViaturaUpdate(LoginRequiredMixin, UpdateView):
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
class GuarnicaoUpdate(LoginRequiredMixin, UpdateView):
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
class PessoaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"P1"
    model = Pessoa
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Pessoas"
        return contexto


# DELETE - ARMA ========================================================================================================
class ArmaDelete(LoginRequiredMixin, DeleteView):
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
class RegistroRMBDelete(LoginRequiredMixin, DeleteView):
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
class ContatoDelete(LoginRequiredMixin, DeleteView):
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
class EnderecoDelete(LoginRequiredMixin, DeleteView):
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
class ViaturaDelete(LoginRequiredMixin, DeleteView):
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
class GuarnicaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    template_name = 'appCadastros/form-excluir.html'
    success_url = reverse_lazy('listar-guarnicao')

    def get_context_data(self, *args, **kwargs):
            contexto = super().get_context_data(*args, **kwargs)
            contexto['titulo'] = "Deletar registro de Guarnição"
            return contexto


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
