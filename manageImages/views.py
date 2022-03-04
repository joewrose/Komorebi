import datetime

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm


def index(request):
    return render(request, 'manageImages/imageCloseup.html')


def closeup(request):
    return render(request, 'manageImages/imageCloseup.html')


def addimage(request):
    form = ImageForm(request.POST, request.FILES)
    print(form.is_bound)

    if request.method == "POST":
        if form.is_valid():
            form.time = datetime.datetime.now()
            picture = form.save(commit=False)
            picture.save()
            return redirect("/closeup/")
        elif request.POST:
            print("ERROR IN FORM")
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'manageImages/addImage.html', context)
