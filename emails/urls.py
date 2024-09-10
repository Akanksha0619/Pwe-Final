from django.urls import path
from .views import send_email, inbox,sent

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('inbox/', inbox, name='inbox'),
    path('sent/',sent,name='sent'),
]
