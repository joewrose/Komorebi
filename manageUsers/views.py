import datetime
from .models import CustomUser
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from manageUsers.models import CustomUser, Follow
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from manageImages.models import Picture, Like, Dislike
from django.db.models import Count
from manageUsers.forms import PostForm, EditForm
from django.contrib.auth.hashers import check_password
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm
from manageImages.models import Picture


def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")


# def myfeed(request):
#     if not request.user.is_authenticated:
#         redirect('/home/')
#
#     context_dict = {}
#
#     pictures = Picture.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]
#
#     context_dict["pictures"] = pictures
#     context_dict["title"] = "My Feed"
#     return render(request, "myfeed.html", context_dict)


def myfeed(request):
    to_recommend = []

    if not request.user.is_authenticated:
        redirect('/home')

    else:
        current_user = request.user
        current_user_liked = Like.objects.values('picture_ID').filter(user_ID=current_user)
        current_user_disliked = Dislike.objects.values('picture_ID').filter(user_ID=current_user)

        # if the current user has liked less than 5 pictures, return None value
        if len(current_user_liked) < 5:
            context_dict = {'myfeed_pictures': None}

        else:
            # create list for the recommended pictures

            # get list of users
            users = CustomUser.objects.all()
            users_checked = 0

            for us in users:
                # stop after pictures from 30 users has been added
                if users_checked <= 30:
                    if us != current_user:
                        user_likes = Like.objects.values('picture_ID').filter(user_ID=us)
                        if len(user_likes) > 5:
                            similar = 0
                            # get the amount of pictures that have been liked by both
                            for pic in user_likes:
                                if pic in current_user_liked:
                                    similar += 1
                            print(len(user_likes))



                            # if the amount of pictures liked by both is a least a third of the current user's liked pictures
                            # add to 'to_recommend' list as long as the picture is not:
                            # already in 'to_recommend', already been liked by the current user, already been disliked by the current user



                            for picture in user_likes:
                                print("IMAGES")
                                pict = Picture.objects.filter(ID=picture['picture_ID'])
                                print(pict)
                                if (pict not in to_recommend) and (pict not in current_user_liked) and (pict not in current_user_disliked):
                                    to_recommend.append(pict)
                                    print(pict)
                                    users_checked += 1
                    else:
                        continue
                else:
                    break


        print(to_recommend)
        # check if list contains pictures
        if to_recommend == []:
            context_dict = {'pictures': "empty"}
        else:
            context_dict = {'pictures': to_recommend}

        return render(request, 'myfeed.html', context=context_dict)


def dashboard(request):
    if not request.user.is_authenticated:
        redirect('/home/')
    context_dict = {}

    pictures = Picture.objects.filter(uploadedBy=request.user)
    if pictures:
        pictures = pictures[:9]
        context_dict["pictures"] = pictures
    else:
        print("NO PICTURES")

    context_dict['pictures'] = None
    context_dict["title"] = "Dashboard"
    return render(request, "dashboard.html", context=context_dict)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("myfeed/")
        else:
            messages.success(request, "There was an error logging you in, try again")
            return redirect("login")

    context_dict = {}
    context_dict["title"] = "My Feed"
    return render(request, "login.html", context=context_dict)


class edit(CreateView):
    model = CustomUser
    form_class = EditForm
    template_name = 'editUser.html'

    def form_valid(self, form):
        formUser = form.save(commit=False)
        user = CustomUser.objects.get(username=self.request.user.username)
        user.email = formUser.email
        user.profileImage = formUser.profileImage
        user.city = formUser.city
        user.description = formUser.description
        form.instance.set_password(form.cleaned_data['password'])
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')

    def get_context_data(self, form=None):
        context = super().get_context_data()
        context["title"] = "Edit Profile"
        return context


def profile(request, username):
    context_dict = {}

    user = CustomUser.objects.get(username=username)

    try:
        follow = Follow.objects.get(followed_ID=user, follower_ID=request.user)
        buttonText = "Following"
    except ObjectDoesNotExist:
        buttonText = "Follow"

    pictures = Picture.objects.filter(uploadedBy=user)

    context_dict["profileUser"] = user
    context_dict['pictures'] = pictures
    context_dict["title"] = "Profile"
    context_dict["buttontext"] = buttonText
    return render(request, "profile.html", context=context_dict)


class create(CreateView):
    model = CustomUser
    form_class = PostForm
    template_name = 'addUser.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        form.instance.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')

    def get_context_data(self, form=None):
        context = super().get_context_data()
        context['title'] = 'Create Account'
        return context


class follow(View):
    @method_decorator(login_required)
    def get(self, request):
        print("GET")
        user = CustomUser.objects.get(id=request.GET['user'])

        if not request.is_ajax:
            raise Http404

        try:
            follow = Follow.objects.get(followed_ID=user, follower_ID=request.user)
            print("DELETING FOLLOW")
            follow.delete()
            buttonText = "Follow"
        except ObjectDoesNotExist:
            print("FOLLOWING")
            follow = Follow.objects.get_or_create(follower_ID=request.user, followed_ID=user)
            buttonText = "Following"

        return HttpResponse(buttonText)


@login_required
def userdelete(request):
    u = CustomUser.objects.get(username=request.user.username)
    u.delete()
    messages.success(request, "The user is deleted")
    return redirect('/home/')
