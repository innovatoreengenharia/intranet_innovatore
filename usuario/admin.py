from django.contrib import admin
from .models import Perfil, Experiencia, Formacao

class ListandoPerfil(admin.ModelAdmin):
    list_display = ('usuario', 'nome')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = 10
admin.site.register(Perfil, ListandoPerfil)


class listandoExperiencia(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('perfil', 'empresa')
    list_per_page = 10
admin.site.register(Experiencia, listandoExperiencia)


class listandoFormacao(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('perfil', 'diploma')
    list_per_page = 10
admin.site.register(Formacao, listandoFormacao)
