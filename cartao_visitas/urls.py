from django.urls import path
from .views import cartao_visitas

urlpatterns = [
    path("", cartao_visitas, name='cartao_visitas'),
]