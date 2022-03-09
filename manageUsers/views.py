import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm

def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")

def dashboard(request):
    return HttpResponse("Welcome to the manageUsers Dashboard page!")