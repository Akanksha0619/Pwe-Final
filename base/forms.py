# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ContactSubmission

class CustomLoginForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin')])

# forms.py
from django import forms
from .models import ContactSubmission



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
