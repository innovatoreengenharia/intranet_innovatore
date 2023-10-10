from django.contrib import admin
from .models import Cartao_visitas

class ListandoCartaoVisitas(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'email', 'site')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ( 'nome',)
    list_per_page = 15

admin.site.register(Cartao_visitas, ListandoCartaoVisitas)
