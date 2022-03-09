import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm


def closeup(request):
    return render(request, 'manageImages/imageCloseup.html')


def dashboard(request):
    return addimage(request)


