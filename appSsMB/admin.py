from django.contrib import admin

from .models import Arma, RegistroRMB

@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('numero'),
    search_fields = ('tipo'),


@admin.register(RegistroRMB)
class RegistroRMBAdmin(admin.ModelAdmin):
    list_display = ('arma'),
    search_fields = ('policial'),
