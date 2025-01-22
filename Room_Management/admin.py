from django.contrib import admin
from .models import *

# Register your models here.

# Registering Room and Booking models to make them manageable via the Django admin interface
admin.site.register(Room)
admin.site.register(Booking)

# Registering Facility model with customized admin display
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Facility model.
    This class modifies how Facility data is displayed and managed in the admin panel.
    """
    list_display = ('facility_name', 'facility_image')  # Columns to display in the admin list view
    search_fields = ('facility_name',)  # Enables search functionality based on facility_name
