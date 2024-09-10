from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='User_create_post'),
    path('', views.post_list, name='User_post_list'),
    path('<int:pk>/update/', views.update_post, name='User_update_post'),
    path('<int:pk>/delete/', views.delete_post, name='User_delete_post'),
]
