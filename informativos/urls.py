from django.urls import path
from . import views

urlpatterns = [
    path("", views.informativos, name="informativos"),
    path("noticia/<int:id>", views.noticia, name="informativos/noticia"),
    path("criar_noticia/", views.criar_noticia, name="informativos/criar_noticia"),
    path("add_noticia/", views.add_noticia, name="informativos/add_noticia"),
    path(
        "criar_comunicado/",
        views.criar_comunicado,
        name="informativos/criar_comunicado",
    ),
]
