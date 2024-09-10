from django.contrib import admin
from .models import Ticket

# Registering the Ticket model with the admin site
admin.site.register(Ticket)
