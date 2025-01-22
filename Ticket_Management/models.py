from django.db import models
from django.contrib.auth.models import User

# Ticket status choices
STATUS_CHOICES = [
    ('arrived', 'Arrived'),            # Ticket has arrived for processing
    ('working', 'Working'),            # Ticket is currently being worked on
    ('solved', 'Solved'),              # Ticket has been resolved
]

# Common issue choices
ISSUE_CHOICES = [
    ('Furnished Rooms', 'Furnished Rooms'),        # Issues related to furnished rooms
    ('Wi-Fi Connectivity', 'Wi-Fi Connectivity'), # Issues related to Wi-Fi connectivity
    ('Clean Drinking Water', 'Clean Drinking Water'), # Issues related to clean drinking water
    ('Washing Machine', 'Washing Machine'),        # Issues related to washing machine
]

"""
This file contains the models for managing support tickets within the application.
It defines the Ticket model with fields for user association, issue type, custom issues, status, and timestamps.
"""

# Ticket Model
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ticket raised by a user
    issue_type = models.CharField(max_length=50, choices=ISSUE_CHOICES)  # Type of issue
    custom_issue = models.CharField(max_length=255, blank=True, null=True)  # Field for custom issues, optional
    description = models.TextField()  # Detailed description of the issue
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='arrived')  # Current status of the ticket
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the ticket is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the ticket is last updated

    def __str__(self):
        return f'{self.user.username} - {self.get_issue_type_display()} - {self.status}'

