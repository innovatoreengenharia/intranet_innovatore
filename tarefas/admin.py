from django.contrib import admin
from .models import Quadros, Colunas, Tarefas


""" class NoticiasAdmin(admin.ModelAdmin):
    list_display = ("titulo", "destaque", "publicado_em", "destaque")
    list_display_links = ("titulo",)
    search_fields = ("titulo", "destaque")
    list_filter = ("titulo", "destaque")
    list_per_page = 10 """


admin.site.register(Quadros)

admin.site.register(Colunas)

admin.site.register(Tarefas)