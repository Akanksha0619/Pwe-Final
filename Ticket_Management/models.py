from django.db import models
from django.contrib.auth.models import User

# Ticket status choices
STATUS_CHOICES = [
    ('arrived', 'Arrived'),
    ('working', 'Working'),
    ('solved', 'Solved'),
]

# Common issue choices
ISSUE_CHOICES = [
    ('Furnished Rooms', 'Furnished Rooms'),
    ('Wi-Fi Connectivity', 'Wi-Fi Connectivity'),
    ('Clean Drinking Water', 'Clean Drinking Water'),
    ('Washing Machine', 'Washing Machine'),
]

# Ticket Model
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ticket raised by
    issue_type = models.CharField(max_length=50, choices=ISSUE_CHOICES)
    custom_issue = models.CharField(max_length=255, blank=True, null=True)  # For custom issues
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='arrived')  # Default status
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set to now on update

    def __str__(self):
        return f'{self.user.username} - {self.get_issue_type_display()} - {self.status}'
