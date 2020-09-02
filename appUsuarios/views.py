from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class UsuarioCreate(CreateView):
    template_name = 'appCadastros/form.html'
    model = User
    fields = ['username', 'email', 'password']

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['titulo'] = "Registrar Novo Usuário"
        contexto['botao'] = "Resgistrar"
        return contexto