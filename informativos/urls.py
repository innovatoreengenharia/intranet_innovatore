from django.urls import path
from . import views

urlpatterns = [
    path("", views.informativos, name="informativos"),
    path("noticia/<int:id>", views.noticia, name="informativos/noticia"),
    path(
        "editar_noticia/<int:id>",
        views.editar_noticia,
        name="informativos/editar_noticia",
    ),
    path(
        "deletar_noticia/<int:id>",
        views.deletar_noticia,
        name="deletar_noticia",
    ),
    path("criar_noticia/", views.criar_noticia, name="informativos/criar_noticia"),
    path("add_noticia/", views.add_noticia, name="informativos/add_noticia"),
    path("todas_noticias/", views.todas_noticias, name="informativos/todas_noticias"),
    path(
        "criar_comunicado/",
        views.criar_comunicado,
        name="informativos/criar_comunicado",
    ),
    path(
        "editar_comunicado/<int:id_comunicado>",
        views.editar_comunicado,
        name="informativos/editar_comunicado",
    ),
    path(
        "deletar_comunicado/<int:id>",
        views.deletar_comunicado,
        name="deletar_comunicado",
    ),
    path(
        "todos_comunicados/",
        views.todos_comunicados,
        name="informativos/todos_comunicados",
    ),
    path("criar_quadro/", views.criar_quadro, name="informativos/criar_quadro"),
    path(
        "editar_quadro/<int:id_quadro>",
        views.editar_quadro,
        name="informativos/editar_quadro",
    ),
    path(
        "todos_quadros/",
        views.todos_quadros,
        name="informativos/todos_quadros",
    ),
    path(
        "deletar_quadro/<int:id>",
        views.deletar_quadro,
        name="deletar_quadro",
    ),
    path("quadro/<int:id_quadro>", views.quadro, name="informativos/quadro"),
]
