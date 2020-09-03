from django.contrib import admin

from .models import Pessoa, Arma, RegistroRMB, Contato, Endereco, Viatura, Guarnicao

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    list_filter = ('matricula'),
    search_fields = ('nome_guerra'),

@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    list_filter = ('especie'),
    search_fields = ('numero'),

@admin.register(RegistroRMB)
class RegistroRMBAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    list_filter = ('data'),
    search_fields = ('policial'),

admin.site.register(Contato)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    list_filter = ('cidade'),
    search_fields = ('cidade'),

admin.site.register(Viatura)
# admin.site.register(Guarnicao)
@admin.register(Guarnicao)
class GuarnicaoAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    list_filter = ('data'),
    search_fields = ('vtr'),