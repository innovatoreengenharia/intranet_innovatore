from django.contrib import admin
from .models import Noticia, Bloco, Comunicado


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ("titulo", "destaque", "publicado_em", "destaque")
    list_display_links = ("titulo",)
    search_fields = ("titulo", "destaque")
    list_filter = ("titulo", "destaque")
    list_per_page = 10


admin.site.register(Noticia, NoticiasAdmin)

admin.site.register(Bloco)

admin.site.register(Comunicado)
