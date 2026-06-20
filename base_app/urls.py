from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Authentication (HTML)
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    # Rooms
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),

    # User/Profile
    path('profile/', views.profile, name='profile'),
    path('update/', views.updateUser, name='update-user'),
    path('delete/', views.deleteUser, name='delete-user'),

    # Topics
    path('topics/', views.topics, name='topics'),
]