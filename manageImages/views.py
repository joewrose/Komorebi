from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm


def index(request):
    return render(request, 'manageImages/imageCloseup.html')


def closeup(request):
    return render(request, 'manageImages/imageCloseup.html')


def addimage(request):
    form = ImageForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'manageImage/addImage.html', context)
