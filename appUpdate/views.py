from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from appCreate.models import Viatura, Guarnicao

class Update(TemplateView):
    template_name = "appUpdate/home.html"




# ATUALIZAR - ARMA =====================================================================================================

# ATUALIZAR - REGISTRO RMB =============================================================================================









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
