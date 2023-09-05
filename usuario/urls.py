from django.urls import path
from .views import cadastro, perfil, editPerfil

urlpatterns = [
    path("cadastro/", cadastro, name='cadastro'),
    path("perfil/", perfil, name='perfil'),
    path("editar/<int:id>", editPerfil, name='editar'),
]