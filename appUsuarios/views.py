from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil


class PerfilCreate(CreateView):
    template_name = 'appCreate/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Registro de novos usuários"
        contexto['botao'] = "Resgistrar"
        return contexto

    def form_valid(self, form):
        url = super().form_valid(form)

        self.object.save()
        Perfil.objects.create(usuario=self.object)

        return url


class PerfilUpdate(UpdateView):
    template_name = "appCreate/form.html"
    model = Perfil
    fields = ['nomeCompletoUsuario', 'matriculaUsuario', 'telefoneUsuario', 'usuario']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Meus dados pessoais"
        contexto['botao'] = "Atualizar Perfil"
        return contexto