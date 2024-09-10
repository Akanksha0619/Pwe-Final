# from django.shortcuts import render

# # Create your views here.

# def admin_leave_requests(request):
#     leave_requests = Leave.objects.all()
#     return render(request, 'admin_leave_requests.html', {'leave_requests': leave_requests})
# # 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from .models import Ticket




# List tickets
@login_required
def view_all_tickets(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()
        

    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'support/ticket_list.html', {'tickets': tickets})


# Raise a new ticket
@login_required
def raise_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('raise_ticket')
    else:
        form = TicketForm()
    return render(request, 'support/raise_ticket.html', {'form': form})

# View a ticket detail (for admin)
@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        ticket.status = status
        ticket.save()
        return redirect('ticket_detail', ticket_id=ticket_id)
    return render(request, 'support/ticket_detail.html', {'ticket': ticket})
