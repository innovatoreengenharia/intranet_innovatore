from django.contrib import admin
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies

class ListandoPerfil(admin.ModelAdmin):
    list_display = ('id','usuario', 'nome')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = 10
admin.site.register(Perfil, ListandoPerfil)


class listandoExperiencia(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('id','perfil', 'empresa')
    list_per_page = 10
admin.site.register(Experiencia, listandoExperiencia)


class listandoFormacao(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('id','perfil', 'diploma')
    list_per_page = 10
admin.site.register(Formacao, listandoFormacao)

class listandoCursos(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('id','perfil', 'nome_certificado',)
    list_per_page = 10
admin.site.register(Cursos, listandoCursos)


class listandoHabilidades(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('id','perfil', 'habilidades')
    list_per_page = 10
admin.site.register(Habilidades, listandoHabilidades)

class listandoHobbies(admin.ModelAdmin):
    list_filter = ('perfil',)
    list_display = ('id','perfil', 'hobbies')
    list_per_page = 10
admin.site.register(Hobbies, listandoHobbies)
