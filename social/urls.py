from django.urls import path
from .views import social, contatos, excluir_post, excluir_comentario

urlpatterns = [
    path("", social, name='social'),
    path("contatos/", contatos, name='contatos'),
    path("excluir_post/<int:post_id>", excluir_post, name='excluir_post'),
    path("excluir_comentario/<int:post_id>", excluir_comentario, name='excluir_comentario'),
]