from django.contrib import admin
from .models import *

# Registering the 'Profile' model with Django's admin interface
# This allows the Profile model to be managed from the Django admin panel
admin.site.register(Profile)
