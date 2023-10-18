from django.urls import path
from .views import social, contatos

urlpatterns = [
    path("", social, name='social'),
    path("contatos/", contatos, name='contatos'),
]