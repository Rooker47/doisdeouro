from django.contrib import admin

from .models import Pessoa, Contato, Endereco, Viatura, Guarnicao

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


@admin.register(Viatura)
class ViaturaRMBAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    search_fields = ('patrimonio'),
    list_filter = ('placa'),


@admin.register(Guarnicao)
class GuarnicaoRMBAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    search_fields = ('data'),
    list_filter = ('vtr'),
