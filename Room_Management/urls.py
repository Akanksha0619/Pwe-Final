from django.urls import path
from .views import *

# Define the URL patterns for the application
urlpatterns = [
    # List all rooms
    path('room_list/', room_list, name='room_list'),

    # Add a new room
    path('add/', add_room, name='add_room'),

    # Edit details of an existing room using its ID
    path('edit/<int:room_id>/', edit_room, name='edit_room'),

    # Delete a room using its ID
    path('delete/<int:room_id>/', delete_room, name='delete_room'),

    # Search for available rooms based on criteria
    path('search/', search_rooms, name='search_rooms'),

    # List of rooms for users
    path('rooms/', User_room_list, name='User_room_list'),

    # View details of a specific room for users
    path('rooms/<int:room_id>/', User_room_detail, name='User_room_detail'),

    # Allow users to book a specific room
    path('rooms/<int:room_id>/book/', create_booking, name='User_book_room'),

    # List all facilities
    path('facilities/', facility_list, name='facility_list'),

    # Add a new facility
    path('facilities/add/', add_facility, name='add_facility'),

    # Edit details of an existing facility using its ID
    path('facilities/edit/<int:facility_id>/', edit_facility, name='edit_facility'),

    # Delete a facility using its ID
    path('facilities/delete/<int:facility_id>/', delete_facility, name='delete_facility'),

    # Admin view of all bookings
    path('admin/bookings/', admin_booking_list, name='admin_booking_list'),
]
