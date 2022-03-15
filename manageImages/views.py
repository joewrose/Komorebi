import datetime
import uuid

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from manageImages.models import Picture

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def closeup(request, ID):

    context_dict = {}
    content = open("static/quote.txt", 'r').read()
    context_dict["quote"] = content

    try:
        picture = Picture.objects.get(ID=uuid.UUID(ID))

        context_dict["picture"] = picture
        context_dict["message"] = "success"

    except Picture.DoesNotExist:

        context_dict["Picture"] = None
        context_dict["message"] = "failure"

    return render(request, 'manageImages/imageCloseup.html', context=context_dict)


def dashboard(request):
    return addimage(request)


def addimage(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        picture = form.save(commit=False)
        print(picture)
        picture.time = datetime.datetime.now()
        picture.id = uuid.uuid4()
        picture.uploadedBy = request.user
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
