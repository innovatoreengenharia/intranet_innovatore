from django.urls import path
from .views import tarefas, quadro, adicionar_participante, remover_participante,alterar_titulo_quadro


urlpatterns = [
    path("", tarefas , name="tarefas"),
    path("quadro/<int:id_quadro>", quadro, name="quadro"),
    path("alterar_titulo_quadro<int:id_quadro>",alterar_titulo_quadro, name="alterar_titulo_quadro"),
    path("adicionar_participante/<int:id_quadro>", adicionar_participante, name="adicionar_participante"),
    path("remover_participante/<int:id_quadro>/<int:id_usuario>", remover_participante, name="remover_participante"),


]