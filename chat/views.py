from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Renamed login to avoid conflict
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Room,Message

@login_required(login_url='login')  # Added login_url argument to redirect to login page if not authenticated
def index(request):
    users = User.objects.all().exclude(username=request.user.username)
    return render(request, "chat/index.html", {"users": users})

@login_required(login_url='login')
def room(request, room_name):
    users = User.objects.all().exclude(username=request.user.username)
    
    # Fetch the room object
    room = Room.objects.get(id=room_name)
    
    # Fetch all messages for this room, ordered by creation date
    messages = Message.objects.filter(room=room).order_by('created_date')

    return render(request, "chat/room_v2.html", {
        "room_name": room_name,
        "room": room,
        "users": users,
        "messages": messages
    })

@login_required(login_url='login')  # Added login_url argument to redirect to login page if not authenticated
def start_chat(request, username):
    second_user = User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user, second_user=second_user)
       
    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user, first_user=second_user)
        except:

           room = Room.objects.create(first_user=request.user, second_user=second_user)
    return redirect("room", room.id)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from .models import Room, Message

from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Room
@login_required
def delete_chat(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Check if the user is either the first_user or second_user
    if request.user != room.first_user and request.user != room.second_user:
        return HttpResponseForbidden("You are not allowed to delete this chat.")

    if request.method == 'GET':
        room.delete()
        return redirect('index')
    
    return JsonResponse({'status': 'Invalid request'}, status=400)
from django.shortcuts import render, get_object_or_404
from .models import  Room
from Admin_Management.models import Profile

def second_user_profile_view(request, room_id):
    # Room instance ko fetch kar rahe hain
    room = get_object_or_404(Room, id=room_id)
    # Second user ka profile get kar rahe hain
    profile = get_object_or_404(Profile, user=room.second_user)
    
    context = {
        'username': profile.user.username,
        'email': profile.email,
        'contact_number': profile.contact_number,
        'address': profile.address,
        'age': profile.age,
        'profile_img_url': profile.profile_img.url,
    }
    
    return render(request, 'chat/second_user_profile_detail.html', context)