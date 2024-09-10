from django.urls import path
from . import views

urlpatterns = [
    
     path('tickets/', views.view_all_tickets, name='ticket_list'),
    path('raise-ticket/', views.raise_ticket, name='raise_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
   
    
]
