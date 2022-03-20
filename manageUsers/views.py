import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.db.models import Count

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")

def myfeed(request):
    context_dict = {}

    pictures = Picture.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]

    for image in pictures:
        print(image)

    context_dict["pictures"] = pictures
    return render(request, "myfeed.html", context_dict)

def dashboard(request):
    return HttpResponse("Welcome to the manageUsers Dashboard page!")

def login(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "login.html", context={"register_form": form})

def edit(request):
    return HttpResponse("Welcome to the manageUsers Edit page!")

def profile(request):
    return HttpResponse("Welcome to the manageUsers Profile page!")

def create(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "addUser.html", context={"register_form": form})
