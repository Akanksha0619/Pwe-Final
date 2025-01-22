from django import forms
from .models import Room, Booking, Facility

class BookingForm(forms.ModelForm):
    """
    Form for creating and editing bookings.
    Allows users to select a user, room, start date, end date, and provide an inquiry.
    """
    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date', 'inquiry']  # Fields included in the form
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',  # Adds Bootstrap class for styling
            }),
            'room': forms.Select(attrs={
                'class': 'form-control',  # Dropdown for selecting room
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select start date',  # Placeholder for date input
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select end date',  # Placeholder for date input
            }),
            'inquiry': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your inquiry here',  # Placeholder for inquiry
                'rows': 4,  # Textarea height
            }),
        }
        labels = {
            'user': 'User',  # Label for user field
            'room': 'Room',  # Label for room field
            'start_date': 'Start Date',  # Label for start date field
            'end_date': 'End Date',  # Label for end date field
            'inquiry': 'Inquiry Details',  # Label for inquiry field
        }


class RoomForm(forms.ModelForm):
    """
    Form for creating and editing room details.
    Allows input for room number, available seats, type, availability date, and floor.
    """
    class Meta:
        model = Room
        fields = ['room_number', 'available_seat', 'type', 'available_date', 'floor']  # Fields included in the form


class FacilityForm(forms.ModelForm):
    """
    Form for creating and editing facilities.
    Includes fields for the facility name and optional image.
    """
    class Meta:
        model = Facility
        fields = ['facility_name', 'facility_image']  # Fields included in the form
