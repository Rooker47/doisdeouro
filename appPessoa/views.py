from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy


class PessoaInfo(TemplateView):
    template_name = "appPessoa/home.html"

# ================================================ SEÇÃO ENTRADA =======================================================
# INFO - PESSOA ======================================================================================================
