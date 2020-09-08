from django.contrib import admin

from .models import Entrada, Saida, Saldo

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('__str__'),
    search_fields = ('nomeMaterialEntrada'),
