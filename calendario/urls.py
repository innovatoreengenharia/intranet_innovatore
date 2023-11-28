from django.urls import path
from . import views

urlpatterns = [
    path("", views.calendario, name="calendario"),
    path("all_events/", views.all_events, name="all_events"),
    path("add_event/", views.add_event, name="add_event"),
    path("update/", views.update, name="update"),
    path("remove/", views.remove, name="remove"),
]
