# urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('room_list/', room_list, name='room_list'),
    path('add/', add_room, name='add_room'),
    path('edit/<int:room_id>/', edit_room, name='edit_room'),
    path('delete/<int:room_id>/', delete_room, name='delete_room'),
    path('search/', search_rooms, name='search_rooms'),
    path('rooms/', User_room_list, name='User_room_list'),
    path('rooms/<int:room_id>/', User_room_detail, name='User_room_detail'),
    path('rooms/<int:room_id>/book/', create_booking, name='User_book_room'),
    path('facilities/',facility_list, name='facility_list'),
     path('facilities/add/', add_facility, name='add_facility'),
    path('facilities/edit/<int:facility_id>/', edit_facility, name='edit_facility'),
    path('facilities/delete/<int:facility_id>/',delete_facility, name='delete_facility'),
    path('admin/bookings/', admin_booking_list, name='admin_booking_list'),
]


