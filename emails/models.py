from django.contrib.auth.models import User
from django.db import models

class Email_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    subject = models.CharField(max_length=255)
    sender = models.EmailField()
    recipient = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    is_sent = models.BooleanField(default=False)
