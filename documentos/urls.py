from django.urls import path
from .views import documentos, qualidade

urlpatterns = [
    path("", documentos , name='documentos'),
    path("qualidade/", qualidade, name='documentos/qualidade')
]