from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=50)
    available_seat = models.IntegerField()
    TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
        ('customized', 'Customized'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    available_date = models.DateField(null=True,blank=True)
    floor = models.IntegerField()

    def __str__(self):
        return self.room_number

# models.py
from django.db import models

class Facility(models.Model):

    facility_name = models.CharField(max_length=100,blank=True, null=True)
    facility_image = models.ImageField(upload_to='facility_images/', blank=True, null=True)

    def __str__(self):
        return self.facility_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    inquiry = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} booking {self.room.room_number} from {self.start_date} to {self.end_date}"

