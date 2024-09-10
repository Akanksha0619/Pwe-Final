from django import forms
from .models import Ticket

# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['issue_type', 'custom_issue', 'description']
        widgets = {
            'issue_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select issue type'
            }),
            'custom_issue': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Custom issue (if any)',
                'maxlength': 100
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your issue...',
                'maxlength': 500,
                'style': 'resize:none;'
            }),
        }
        labels = {
            'issue_type': 'Issue Type',
            'custom_issue': 'Custom Issue (Optional)',
            'description': 'Issue Description',
        }
