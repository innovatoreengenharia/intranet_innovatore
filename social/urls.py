from django.urls import path
from .views import social, contatos, excluir_post

urlpatterns = [
    path("", social, name='social'),
    path("contatos/", contatos, name='contatos'),
    path("excluir_post/<int:post_id>", excluir_post, name='excluir_post'),
]