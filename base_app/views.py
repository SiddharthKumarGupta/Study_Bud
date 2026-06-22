# ==========================================================
# IMPORTS
# ==========================================================

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.models import User

from .models import Room, Topic, Message
from .forms import MyUserCreationForm, RoomForm


# ==========================================================
# HOME PAGE
# ==========================================================

def home(request):
    """
    Display all rooms, topics and recent messages.
    Supports searching rooms by topic.
    """

    q = request.GET.get("q", "")

    rooms = Room.objects.filter(
        topic__name__icontains=q
    )

    topics = Topic.objects.annotate(
        room_count=Count("room")
    )

    room_count = rooms.count()

    room_messages = Message.objects.filter(
        room__topic__name__icontains=q
    )[:5]

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count,
        "messages": room_messages,
        "q": q,
    }

    return render(request, "base_app/home.html", context)


# ==========================================================
# LOGIN
# ==========================================================

def loginPage(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid Username or Password")

    return render(request, "base_app/login.html")


# ==========================================================
# REGISTER
# ==========================================================

def registerPage(request):

    form = MyUserCreationForm()

    if request.method == "POST":

        form = MyUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            return redirect("home")

    return render(
        request,
        "base_app/signup.html",
        {"form": form},
    )


# ==========================================================
# LOGOUT
# ==========================================================

def logoutUser(request):
    logout(request)
    return redirect("home")


# ==========================================================
# PROFILE PAGE
# ==========================================================

@login_required
def profile(request):

    context = {
        "user": request.user
    }

    return render(
        request,
        "base_app/profile.html",
        context,
    )


# ==========================================================
# UPDATE PROFILE
# ==========================================================

@login_required
def updateUser(request):

    user = request.user

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()

        if not username:
            messages.error(request, "Username cannot be empty.")
            return redirect("update-user")

        user.username = username
        user.email = email

        user.save()

        messages.success(request, "Profile Updated Successfully!")

        return redirect("profile")

    return render(
        request,
        "base_app/update.html",
        {"user": user}
    )


# ==========================================================
# DELETE ACCOUNT
# ==========================================================

@login_required
def deleteUser(request):

    if request.method == "POST":

        request.user.delete()

        return redirect("home")

    return render(
        request,
        "base_app/delete.html",
    )


# ==========================================================
# CREATE ROOM
# ==========================================================

@login_required
def createRoom(request):

    form = RoomForm()

    if request.method == "POST":

        form = RoomForm(request.POST)

        if form.is_valid():

            room = form.save(commit=False)

            room.host = request.user

            room.save()

            return redirect(
                "room",
                pk=room.id
            )

    context = {
        "form": form
    }

    return render(
        request,
        "base_app/room_form.html",
        context,
    )


# ==========================================================
# ROOM DETAILS + CHAT
# ==========================================================

def room(request, pk):

    room = get_object_or_404(Room, id=pk)

    room_messages = room.message_set.all().order_by("-created")

    participants = room.participants.all()

    if request.method == "POST":

        if request.user.is_authenticated:

            body = request.POST.get("body")

            if body:

                Message.objects.create(
                    user=request.user,
                    room=room,
                    body=body,
                )

                room.participants.add(request.user)

        return redirect("room", pk=room.id)

    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }

    return render(
        request,
        "base_app/room.html",
        context,
    )


# ==========================================================
# ROOMS LIST
# ==========================================================

def rooms(request):

    q = request.GET.get("q", "")

    rooms = Room.objects.filter(
        topic__name__icontains=q
    )

    topics = Topic.objects.annotate(
        room_count=Count("room")
    )

    context = {
        "rooms": rooms,
        "topics": topics,
        "q": q,
    }

    return render(
        request,
        "base_app/rooms.html",
        context,
    )


# ==========================================================
# TOPICS PAGE
# ==========================================================

def topics(request):

    q = request.GET.get("q", "")

    topics = Topic.objects.filter(
        name__icontains=q
    ).annotate(
        room_count=Count("room")
    )

    context = {
        "topics": topics,
        "q": q,
    }

    return render(
        request,
        "base_app/topics.html",
        context,
    )


# ==========================================================
# STATIC PAGES
# ==========================================================

def navbar(request):
    return render(
        request,
        "base_app/navbar.html",
    )


def main(request):
    return render(
        request,
        "base_app/main.html",
    )