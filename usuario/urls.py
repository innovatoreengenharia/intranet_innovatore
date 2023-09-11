from django.urls import path
from .views import cadastro, perfil, editPerfil, deletar_hobbie, deletar_formacao, deletar_experiencia, deletar_curso, deletar_habilidade

urlpatterns = [
    path("cadastro/", cadastro, name='cadastro'),
    path("perfil/", perfil, name='perfil'),
    path("editar/<int:id>", editPerfil, name='editar'),
    path("deletar_experiencia/<int:id>", deletar_experiencia, name='deletar_experiencia'),
    path("deletar_formacao/<int:id>", deletar_formacao, name='deletar_formacao'),
    path("deletar_curso/<int:id>", deletar_curso, name='deletar_curso'),
    path("deletar_habilidade/<int:id>", deletar_habilidade, name='deletar_habilidade'),
    path("deletar_hobbie/<int:id>", deletar_hobbie, name='deletar_hobbie'),
]