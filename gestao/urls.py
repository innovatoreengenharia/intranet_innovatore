from django.urls import path
from .views import qualidade

urlpatterns = [
    path("qualidade", qualidade, name='qualidade')
]
