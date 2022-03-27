import datetime
import uuid
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.views import View
from django.http import HttpResponse, Http404
from manageImages.forms import ImageForm
from manageImages.models import Like, Dislike


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

    return render(request, 'imageCloseup.html', context=context_dict)


def dashboard(request):
    return addimage(request)


class addImage(CreateView, LoginRequiredMixin):
    model = Picture
    form_class = ImageForm
    template_name = 'addImage.html'

    def form_valid(self, form):
        print("VALID FORM")
        picture = form.save(commit=False)

        picture.time = datetime.datetime.now()
        picture.ID = uuid.uuid4()
        picture.uploadedBy = self.request.user
        picture.image.upload_to = "/manageImages/" + str(self.request.user.id) + "/" + str(picture.ID)
        picture.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('manageUsers:dashboard')

    def get_context_data(self, form=None):
        context = super().get_context_data()
        context['title'] = 'Add Image'
        return context


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

        if picture.likes.filter(user_ID=request.user.id).exists():
            print("DELETING LIKE")
            like = picture.likes.get(user_ID=request.user.id)
            like.delete()
        else:
            print("ADDING LIKE")
            if picture.dislikes.filter(user_ID=request.user.id).exists():
                print("DELETING DISLIKE")
                dislike = picture.dislikes.get(user_ID=request.user.id)
                dislike.delete()
            like = Like.objects.get_or_create(user_ID=request.user, picture_ID=Picture.objects.get(ID=picture_ID))

        votes = str(picture.dislikes.count()) + ":" + str(picture.likes.count())

        return HttpResponse(votes)


class DislikePictureView(View):
    @method_decorator(login_required)
    def get(self, request):
        picture_ID = request.GET['picture_id']

        if not request.is_ajax:
            raise Http404

        try:
            picture = Picture.objects.get(ID=picture_ID)
        except:
            return HttpResponse(-1)

        if picture.dislikes.filter(user_ID=request.user.id).exists():
            print("DELETING DISLIKE")
            dislike = picture.dislikes.get(user_ID=request.user.id)
            dislike.delete()
        else:
            print("ADDING DISLIKE")
            if picture.likes.filter(user_ID=request.user.id).exists():
                print("DELETING LIKE")
                like = picture.likes.get(user_ID=request.user.id)
                like.delete()
            dislike = Dislike.objects.get_or_create(user_ID=request.user, picture_ID=Picture.objects.get(ID=picture_ID))

        votes = str(picture.dislikes.count()) + ":" + str(picture.likes.count())

        return HttpResponse(votes)
