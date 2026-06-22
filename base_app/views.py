from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm
from .models import Room, Topic,Message
from django.db.models import Q, Count
from .forms import RoomForm
# Create your views here.

# Create home page views here.
def home(request):
    q = request.GET.get('q', '')

    rooms = Room.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()
    room_count = rooms.count()
    messages = Message.objects.filter(room__topic__name__icontains=q)[:5]

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'messages': messages,
    }
    return render(request, 'base_app/home.html', context)



# Create your room views here.



# 🔹 Create Room
@login_required
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('room', pk=room.id)  # Redirect to room detail page

    return render(request, 'base_app/room_form.html', {'form': form})


# 🔹 Room Detail View
def room(request, pk):
    room = get_object_or_404(Room, id=pk)
    messages = room.message_set.all()

    context = {
        'room': room,
        'messages': messages
    }

    return render(request, 'base_app/room.html', context)


# 🔹 Rooms List View
def rooms(request):
    q = request.GET.get('q', '')
    rooms = Room.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()

    context = {
        'rooms': rooms,
        'topics': topics,
    }
    return render(request, 'base_app/rooms.html', context)

# Create your namebar views here.
def navbar(request):
     
     return render(request,'base_app/navebar.html')

# Create your topics views here.
def topics(request):
     
     return render(request,'base_app/topics.html')

def main(request):
     
     return render(request,'base_app/main.html')

# -------------------------
# REGISTER
# -------------------------
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')

    return render(request, 'base_app/signup.html', {'form': form})


# -------------------------
# LOGOUT
# -------------------------
def logoutUser(request):
    logout(request)
    return redirect('home')


# -------------------------
# PROFILE (READ)
# -------------------------
@login_required
def profile(request):
    return render(request, 'base_app/profile.html', {'user': request.user})


# -------------------------
# UPDATE USER
# -------------------------
@login_required
def updateUser(request):
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        messages.success(request, "Profile updated successfully")
        return redirect('profile')

    return render(request, 'base_app/update.html', {'user': user})


# -------------------------
# DELETE USER
# -------------------------
@login_required
def deleteUser(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')

    return render(request, 'base_app/delete.html')

def loginPage(request):
    # prevent logged-in users from accessing login page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'base_app/login.html')

def room(request, pk):

    room = Room.objects.get(id=pk)

    room_messages = room.message_set.all().order_by("-created")

    participants = room.participants.all()

    if request.method == "POST":

        Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )

        room.participants.add(request.user)

        return redirect("room", pk=room.id)

    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }

    return render(request, "base_app/room.html", context)

from django.db.models import Count

def topics(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    topics = Topic.objects.filter(
        name__icontains=q
    ).annotate(room_count=Count('room'))

    context = {
        'topics': topics,
        'q': q,
    }
    return render(request, 'base_app/topics.html', context)