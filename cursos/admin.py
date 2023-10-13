from django.contrib import admin
from .models import Cursos

class ListandoCursos(admin.ModelAdmin):
    list_display = ('nome', 'setor')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ( 'nome',)
    list_per_page = 10
admin.site.register(Cursos, ListandoCursos)