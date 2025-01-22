from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Facility, Booking
from .forms import RoomForm, FacilityForm, BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def add_room(request):
    """
    Handle the creation of a new room.

    If the request method is POST, validate the RoomForm and save it. Otherwise, display an empty RoomForm.
    Redirect to the room list page upon successful creation.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'add_room.html' template or redirect to 'room_list'.
    """
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})


def edit_room(request, room_id):
    """
    Handle editing an existing room.

    Fetch the room by ID and populate the RoomForm. Save changes upon form submission.

    Args:
        request (HttpRequest): The HTTP request object.
        room_id (int): The ID of the room to edit.

    Returns:
        HttpResponse: Rendered 'edit_room.html' template or redirect to 'room_list'.
    """
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
    """
    Handle deleting a room.

    Fetch the room by ID and delete it upon POST request.

    Args:
        request (HttpRequest): The HTTP request object.
        room_id (int): The ID of the room to delete.

    Returns:
        HttpResponse: Rendered 'delete_room.html' template or redirect to 'room_list'.
    """
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'delete_room.html', {'room': room})


def room_list(request):
    """
    Display a list of all rooms.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'room_list.html' template.
    """
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


def search_rooms(request):
    """
    Search for available rooms based on start date and room type.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'search_room.html' template with search results.
    """
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        room_type = request.GET.get('room_type')

        available_rooms = Room.objects.filter(type=room_type, available_seat__gt=0)

        context = {
            'start_date': start_date,
            'room_type': room_type,
            'available_rooms': available_rooms,
        }
        return render(request, 'search_room.html', context)


def User_room_list(request):
    """
    Display a list of rooms for users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'User_room_list.html' template.
    """
    rooms = Room.objects.all()
    return render(request, 'User_room_list.html', {'rooms': rooms})


def User_room_detail(request, room_id):
    """
    Display detailed information about a specific room for users.

    Args:
        request (HttpRequest): The HTTP request object.
        room_id (int): The ID of the room to display.

    Returns:
        HttpResponse: Rendered 'User_room_detail.html' template.
    """
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'User_room_detail.html', {'room': room})


def facility_list(request):
    """
    Display a list of facilities with optional sorting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'facility_list.html' template.
    """
    facilities = Facility.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by in ['facility_type', 'facility_name']:
        facilities = facilities.order_by(sort_by)
    elif sort_by == 'facility_id':
        facilities = facilities.order_by('id')

    return render(request, 'facility_list.html', {'facilities': facilities})


def add_facility(request):
    """
    Handle the creation of a new facility.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'add_facility.html' template or redirect to 'facility_list'.
    """
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'add_facility.html', {'form': form})


def edit_facility(request, facility_id):
    """
    Handle editing an existing facility.

    Args:
        request (HttpRequest): The HTTP request object.
        facility_id (int): The ID of the facility to edit.

    Returns:
        HttpResponse: Rendered 'edit_facility.html' template or redirect to 'facility_list'.
    """
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
    """
    Handle deleting a facility.

    Args:
        request (HttpRequest): The HTTP request object.
        facility_id (int): The ID of the facility to delete.

    Returns:
        HttpResponse: Redirect to 'facility_list'.
    """
    facility = get_object_or_404(Facility, id=facility_id)
    facility.delete()
    return redirect('facility_list')


def create_booking(request, room_id):
    """
    Create a new booking for a specific room.

    Args:
        request (HttpRequest): The HTTP request object.
        room_id (int): The ID of the room to book.

    Returns:
        HttpResponse: Rendered 'User_book_room.html' template or redirect to 'User_room_list'.
    """
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()

            messages.success(request, "Booking successfully created!")
            return redirect('User_room_list')
        else:
            messages.error(request, "Error in booking form. Please correct the errors.")
    else:
        form = BookingForm()

    context = {
        'form': form,
        'room': room,
    }
    return render(request, 'User_book_room.html', context)


@staff_member_required
def admin_booking_list(request):
    """
    Display a list of all bookings for admin users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 'admin_booking_list.html' template.
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'admin_booking_list.html', context)
