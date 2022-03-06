import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def register_request(request):
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


def index(request):
    return render(request, 'manageImages/imageCloseup.html')


def closeup(request):
    return render(request, 'manageImages/imageCloseup.html')


def dashboard(request):
    return addimage(request)


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
