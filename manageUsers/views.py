import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")

def about(request):
    return HttpResponse("Welcome to the manageUsers About page!")

def myfeed(request):
    return HttpResponse("Welcome to the manageUsers My Feed page!")

def dashboard(request):
    return HttpResponse("Welcome to the manageUsers Dashboard page!")

def login(request):
    return HttpResponse("Welcome to the manageUsers Log In page!")

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
