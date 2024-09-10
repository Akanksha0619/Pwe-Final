"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_app', include('Admin_Management.urls')),
    path('',include('base.urls')),
    path('User_Profile/', include('User_Management.urls')),
    path('post/', include('User_Post.urls')),
    path('chat/', include('chat.urls')),
     path('room/', include('Room_Management.urls')),
     path('communication/', include('Chat_System.urls')),
    path('ticket/', include('Ticket_Management.urls')),
    path('emails/',include('emails.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
