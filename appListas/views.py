from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from appCreate.models import Viatura, Guarnicao


class Listas(TemplateView):
    template_name = "appListas/home.html"






# LISTAR - REGISTRO RMB ================================================================================================









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
