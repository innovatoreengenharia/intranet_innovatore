from django.urls import path
from .views import tarefas


urlpatterns = [
    path("", tarefas , name='tarefas'),
]