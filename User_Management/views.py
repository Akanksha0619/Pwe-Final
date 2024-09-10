from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile


@login_required
def user_profile(request):
    profile = request.user.UserProfile
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.age = request.POST.get('age')
        profile.room_number = request.POST.get('room_number')
        profile.bed_number = request.POST.get('bed_number')
        profile.mobile_number = request.POST.get('mobile_number')
        profile.aadhar_card = request.POST.get('aadhar_card')
        profile.pan_card = request.POST.get('pan_card')
        profile.bio = request.POST.get('bio')
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
        profile.save()
        return redirect('user_profile')

    return render(request, 'user_profile.html', {'profile': profile})


@login_required
def update_profile(request):
    profile = request.user.UserProfile  # Fetch the user's profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to profile page after saving
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user_profile.html', {'profile': profile, 'form': form})
