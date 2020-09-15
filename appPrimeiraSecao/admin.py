from django.contrib import admin

from .models import Pessoa, Contato, Endereco

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    search_fields = ('matricula'),


@admin.register(Contato)
class ContatoRMBAdmin(admin.ModelAdmin):
    list_display = ('__str__'),


@admin.register(Endereco)
class EnderecoRMBAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    search_fields = ('idPessoaEndereco'),
    list_filter = ('cidade'),
