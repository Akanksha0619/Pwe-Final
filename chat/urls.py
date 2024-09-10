# chat/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),
    path('start_chat/<str:username>', start_chat, name="start_chat"),
    path('room/<uuid:room_id>/delete/', delete_chat, name='delete_chat'),  # Change `int:room_id` to `uuid:room_id`
    path('second_user_profile/<uuid:room_id>/', second_user_profile_view, name='second_user_profile_view'),

]
