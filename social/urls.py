from django.urls import path
from .views import social, contatos, excluir_post, excluir_comentario, editPost

urlpatterns = [
    path("", social, name='social'),
    path("contatos/", contatos, name='contatos'),
    path("editar_postagem/<int:post_edit_id>", editPost, name='editar_postagem'),
    path("excluir_post/<int:post_id>", excluir_post, name='excluir_post'),
    path("excluir_comentario/<int:post_id>", excluir_comentario, name='excluir_comentario'),
]