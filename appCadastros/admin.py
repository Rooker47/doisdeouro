from django.contrib import admin

from .models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao

admin.site.register(Pessoa)
admin.site.register(Arma)
admin.site.register(RegistroRMB)
admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(Viatura)
admin.site.register(Guarnicao)