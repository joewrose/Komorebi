import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def about(request):
    return render(request, 'about.html')

def index(request):
    return redirect("/home/")

def home(request):
    return render(request, "home.html")

def addimage(request):
    form = ImageForm(request.POST, request.FILES)
    print(form.is_bound)

    if request.method == "POST":
        if form.is_valid():
            form.time = datetime.datetime.now()
            picture = form.save(commit=False)
            print(picture)
            picture.image.upload_to = "/manageImages/" + str(request.user.id) + "/" + str(picture.ID)
            print(picture.image.upload_to)
            picture.save()
            return redirect("/closeup/")
        elif request.POST:
            print("ERROR IN FORM")
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'manageImages/addImage.html', context)
