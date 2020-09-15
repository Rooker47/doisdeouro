from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from appCreate.models import Viatura, Guarnicao


class Delete(TemplateView):
    template_name = "appDelete/home.html"










# DELETE - VIATURA =====================================================================================================
class ViaturaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"STC"
    model = Viatura
    template_name = 'appDelete/form-excluir.html'
    success_url = reverse_lazy('viaturaList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Viatura"
        contexto['botao'] = "Deletar"
        return contexto


# DELETE - GUARNIÇÕES=== ===============================================================================================
class GuarnicaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Central"
    model = Guarnicao
    template_name = 'appDelete/form-excluir.html'
    success_url = reverse_lazy('guarnicaoList')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Deletar registro de Guarnição"
        contexto['botao'] = "Deletar"
        return contexto

