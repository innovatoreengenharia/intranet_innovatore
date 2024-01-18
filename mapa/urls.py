from django.urls import path
from mapa import views

urlpatterns = [
    path("", views.mapa, name="mapa"),
]
