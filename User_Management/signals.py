from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, AdminProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            AdminProfile.objects.get_or_create(user=instance)
        else:
            UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        try:
            profile = instance.userprofile  # Access the related UserProfile instance
            profile.save()  # Save profile if it exists
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)  # Create profile if it does not exist
