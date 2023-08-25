from django.contrib import admin
from .models import *

class ListandoPerfil(admin.ModelAdmin):
    list_display = ('usuario', 'nome')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = 10
    
admin.site.register(Perfil, ListandoPerfil)
