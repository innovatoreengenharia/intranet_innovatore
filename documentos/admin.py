from django.contrib import admin
from .models import Qualidade, Comercial, Controladoria, DepartamentoPessoal, Engenharia, Financeiro, Fiscal, Juridico, Logistica, Marketing, MeioAmbiente, Orcamentos, PMO, RecursosHumanos, SegurancaDoTrabalho, Sistemas, Suprimentos, TI, Vendas

class ListandoComercial(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Comercial, ListandoComercial)

class ListandoControladoria(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Controladoria, ListandoControladoria)

class ListandoDepartamentoPessoal(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(DepartamentoPessoal, ListandoDepartamentoPessoal)

class ListandoEngenharia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Engenharia, ListandoEngenharia)

class ListandoFinanceiro(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Financeiro, ListandoFinanceiro)

class ListandoFiscal(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Fiscal, ListandoFiscal)

class ListandoJuridico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Juridico, ListandoJuridico)

class ListandoLogistica(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Logistica, ListandoLogistica)

class ListandoMarketing(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Marketing, ListandoMarketing)

class ListandoMeioAmbiente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(MeioAmbiente, ListandoMeioAmbiente)

class ListandoOrcamentos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Orcamentos, ListandoOrcamentos)

class ListandoPMO(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(PMO, ListandoPMO)

class ListandoQualidade(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Qualidade, ListandoQualidade)

class ListandoRecursosHumanos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(RecursosHumanos, ListandoRecursosHumanos)

class ListandoSegurancaDoTrabalho(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(SegurancaDoTrabalho, ListandoSegurancaDoTrabalho)

class ListandoSistemas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Sistemas, ListandoSistemas)

class ListandoSuprimentos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Suprimentos, ListandoSuprimentos)

class ListandoTI(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(TI, ListandoTI)

class ListandoVendas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'doc', 'modificado', 'tipo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nome',)
    list_per_page = 10
    
admin.site.register(Vendas, ListandoVendas)

