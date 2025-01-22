from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    """
    Represents a room in the system with details like room number,
    available seats, type of room, availability date, and floor.
    """
    room_number = models.CharField(max_length=50)  # Unique identifier for the room
    available_seat = models.IntegerField()  # Number of available seats in the room
    TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
        ('customized', 'Customized'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)  # Type of room
    available_date = models.DateField(null=True, blank=True)  # Date when the room becomes available
    floor = models.IntegerField()  # Floor number where the room is located

    def __str__(self):
        return self.room_number  # String representation of the room


class Facility(models.Model):
    """
    Represents a facility offered, with an optional image to showcase it.
    """
    facility_name = models.CharField(max_length=100, blank=True, null=True)  # Name of the facility
    facility_image = models.ImageField(upload_to='facility_images/', blank=True, null=True)  # Image of the facility

    def __str__(self):
        return self.facility_name  # String representation of the facility


class Booking(models.Model):
    """
    Represents a booking made by a user for a specific room within a date range.
    Includes additional inquiries related to the booking.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the booking
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Room being booked
    start_date = models.DateField()  # Booking start date
    end_date = models.DateField()  # Booking end date
    inquiry = models.TextField(null=True, blank=True)  # Additional inquiries or notes for the booking

    def __str__(self):
        return f"{self.user.username} booking {self.room.room_number} from {self.start_date} to {self.end_date}"
