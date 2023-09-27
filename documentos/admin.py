from django.contrib import admin
from .models import Qualidade

class ListandoQualidade(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Qualidade, ListandoQualidade)

# Register your models here.
