from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('service/',service, name='service'),
    path('subscribe/', subscribe, name='subscribe'),
    path('base_login/', base_login, name='base_login'),




]
