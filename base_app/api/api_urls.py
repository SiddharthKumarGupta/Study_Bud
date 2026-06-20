from django.urls import path
from . import api_views

urlpatterns = [
    # Auth APIs
    path('register/', api_views.registerUser),
    path('login/', api_views.loginUser),
    path('test/', api_views.testAuth),

    # Rooms API
    path('rooms/', api_views.getRooms),
    path('rooms/<int:pk>/', api_views.getRoom),
    path('topics/', api_views.getTopics),
]