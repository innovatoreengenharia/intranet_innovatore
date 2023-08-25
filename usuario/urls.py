from django.urls import path
from .views import cadastro, perfil

urlpatterns = [
    path("cadastro/", cadastro, name='cadastro'),
    path("perfil/", perfil, name='perfil'),
]