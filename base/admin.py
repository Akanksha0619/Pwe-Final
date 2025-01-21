from django.contrib import admin
from .views import *
from .models import *


admin.site.site_header= "USER"
admin.site.register(Subscription)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)
