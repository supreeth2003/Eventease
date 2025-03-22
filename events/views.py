from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Event  # Assuming you have an Event model
from django.http import HttpResponseForbidden

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("index")  # Redirect to home page or dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})

@login_required
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event_details.html", {"event": event})

@login_required
def add_event(request):
    """Handles adding new events with image upload and associates event with the creator."""
    if request.method == "POST":
        name = request.POST["name"]
        date = request.POST["date"]
        location = request.POST["location"]
        description = request.POST["description"]

        Event.objects.create(
            name=name, 
            date=date, 
            location=location, 
            description=description,
            created_by=request.user  # Associate event with logged-in user
        )
        return redirect("events")

    return render(request, "add_event.html")

@login_required
def edit_event(request, event_id):
    """Allow users to edit only their own events; admin can edit all."""
    event = get_object_or_404(Event, id=event_id)

    # Restrict normal users from editing others' events
    if request.user != event.created_by and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to edit this event.")

    if request.method == "POST":
        event.name = request.POST["name"]
        event.date = request.POST["date"]
        event.location = request.POST["location"]
        event.description = request.POST["description"]
        event.save()
        return redirect("events")

    return render(request, "edit_event.html", {"event": event})

@login_required
def delete_event(request, event_id):
    """Allow users to delete only their own events; admin can delete all."""
    event = get_object_or_404(Event, id=event_id)

    # Restrict normal users from deleting others' events
    if request.user != event.created_by and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this event.")

    if request.method == "POST":
        event.delete()
        return redirect("events")

    return render(request, "event_details.html", {"event": event})
