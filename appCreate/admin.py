from django.contrib import admin

from .models import Viatura, Guarnicao

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
