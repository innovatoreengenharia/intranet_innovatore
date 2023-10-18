from django.urls import path
from .views import aniversariantes

urlpatterns = [
    path("", aniversariantes, name='aniversariantes'),
]