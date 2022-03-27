from django.urls import path

from . import views
urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<slug:room_slug>", views.room, name="room"),
]
