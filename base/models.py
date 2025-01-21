from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# models.py
from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Email unique hai
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically set the submission time

    def __str__(self):
        return f"{self.name} - {self.email}"
