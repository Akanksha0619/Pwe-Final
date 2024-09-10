# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

def edit_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'edit_room.html', {'form': form})

def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'delete_room.html', {'room': room})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


from django.shortcuts import render
from .models import Room


from .models import Room
from django.shortcuts import render, redirect

def search_rooms(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        room_type = request.GET.get('room_type')

        # Perform room availability check based on start date and room type
        available_rooms = Room.objects.filter(type=room_type, available_seat__gt=0)

        context = {
            'start_date': start_date,
            'room_type': room_type,
            'available_rooms': available_rooms,
        }
        return render(request, 'search_room.html', context)






def User_room_list(request):
    rooms = Room.objects.all()
    return render(request, 'User_room_list.html', {'rooms': rooms})

def User_room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'User_room_detail.html', {'room': room})

@login_required
def User_book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect('User_room_list')
    else:
        form = BookingForm()
    return render(request, 'User_book_room.html', {'form': form, 'room': room})




















# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Facility
from .forms import FacilityForm

def facility_list(request):
    facilities = Facility.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by in ['facility_type', 'facility_name']:
        facilities = facilities.order_by(sort_by)
    elif sort_by == 'facility_id':
        facilities = facilities.order_by('id')
    
    return render(request, 'facility_list.html', {'facilities': facilities})
# views.py
from django.shortcuts import render, redirect
from .models import Facility
from .forms import FacilityForm

def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'add_facility.html', {'form': form})


def edit_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'edit_facility.html', {'form': form})

def delete_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    facility.delete()
    return redirect('facility_list')
