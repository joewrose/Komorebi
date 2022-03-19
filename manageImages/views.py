import datetime
import uuid

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.views import View
from django.http import HttpResponse, Http404
from manageImages.forms import ImageForm, NewUserForm
from manageImages.models import Like


def closeup(request, ID):
    context_dict = {}
    content = open("static/quote.txt", 'r').read()
    context_dict["quote"] = content

    if not request.is_ajax:
        return Http404

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


class LikePictureView(View):
    @method_decorator(login_required)
    def get(self, request):
        picture_ID = request.GET['picture_id']

        if not request.is_ajax:
            raise Http404

        try:
            picture = Picture.objects.get(ID=picture_ID)
        except:
            return HttpResponse(-1)

        try:
            picture.likes.get(user_ID=request.user.id)
            print("User has already liked this image")
            return HttpResponse("Likes " + (picture.likes.count()))
        except:
            try:
                dislike = picture.dislikes.get(user_ID=request.user.id)
                dislike.delete()
            except:
                like = Like.objects.get_or_create(user_ID=request.user, picture_ID=Picture.objects.get(ID=picture_ID))

        return HttpResponse("Likes " + str(picture.likes.count()))
