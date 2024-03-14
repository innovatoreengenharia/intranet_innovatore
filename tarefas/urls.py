from django.urls import path

from .views import (
    adicionar_participante,
    alterar_titulo_quadro,
    quadro,
    remover_participante,
    remover_quadro,
    tarefas,
)

urlpatterns = [
    path("", tarefas, name="tarefas"),
    path("quadro/<int:id_quadro>", quadro, name="tarefas/quadro"),
    path(
        "alterar_titulo_quadro<int:id_quadro>",
        alterar_titulo_quadro,
        name="tarefas/alterar_titulo_quadro",
    ),
    path(
        "remover_quadro<int:id_quadro>",
        remover_quadro,
        name="tarefas/remover_quadro",
    ),
    path(
        "adicionar_participante/<int:id_quadro>",
        adicionar_participante,
        name="tarefas/adicionar_participante",
    ),
    path(
        "remover_participante/<int:id_quadro>/<int:id_usuario>",
        remover_participante,
        name="tarefas/remover_participante",
    ),
]
