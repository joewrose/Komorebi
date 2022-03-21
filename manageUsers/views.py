import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.db.models import Count



# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm
from manageImages.models import Picture

def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")

def myfeed(request):
    context_dict = {}

    pictures = Picture.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]

    context_dict["pictures"] = pictures
    return render(request, "myfeed.html", context_dict)

def dashboard(request):
    return HttpResponse("Welcome to the manageUsers Dashboard page!")

def home(request):
    pictures = Picture.objects.orderby('time')
    current_user = request.user.id
    login_pictures = Picture.objects.filter(picture.uploaded_by != current_user).orderby('time')

    context = {'pictures': pictures, 'login_pictures': login_pictures}
    
    return render(request, 'home.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("myfeed/")
        else:
            messages.success(request, "There was an error logging you in, try again")
            return redirect("login")

    return render(request, "login.html")

def edit(request):
    return HttpResponse("Welcome to the manageUsers Edit page!")

def profile(request):
    return HttpResponse("Welcome to the manageUsers Profile page!")

def create(request):

    context_dict = {}

    pictures = Picture.objects.annotate(num_likes=Count('likes'))[:6]

    context_dict["pictures"] = pictures

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    context_dict["register_form"] = form

    return render(request, "addUser.html", context=context_dict)
