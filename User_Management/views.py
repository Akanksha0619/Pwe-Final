from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile

@login_required
def user_profile(request):
    try:
        profile = request.user.userprofile  # Access using related_name
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)  # Create profile if missing

    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        
        # Handle age input properly: if empty, set to None or use a default value
        age = request.POST.get('age')
        if age:
            try:
                profile.age = int(age)  # Convert to integer if not empty
            except ValueError:
                profile.age = None  # Set to None if the value is invalid
        else:
            profile.age = None  # Or set to a default value like 18, if required
        
        profile.room_number = request.POST.get('room_number')
        profile.bed_number = request.POST.get('bed_number')
        profile.mobile_number = request.POST.get('mobile_number')
        profile.aadhar_card = request.POST.get('aadhar_card')
        profile.pan_card = request.POST.get('pan_card')
        profile.bio = request.POST.get('bio')

        # Check if there's a new image uploaded
        if 'image' in request.FILES:
            profile.image = request.FILES['image']

        # Save the updated profile
        profile.save()

        # Redirect to avoid resubmitting the form if refreshed
        return redirect('user_profile')  

    return render(request, 'user_profile.html', {'profile': profile})
