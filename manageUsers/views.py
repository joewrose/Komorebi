import datetime
from .models import CustomUser
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from manageUsers.models import CustomUser, Follow
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.db.models import Count
from manageUsers.forms import PostForm, EditForm
from django.contrib.auth.hashers import check_password
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.http import HttpResponse, Http404

from manageImages.forms import ImageForm
from manageImages.models import Picture, Like, Dislike


def myfeed(request):
    # if the current user is not logged in, redirect them to the home page
    if not request.user.is_authenticated:
        return redirect('/home/')

    else:
        # create context dictionary
        context_dict = {}

        # get the current logged in user
        current_user = request.user

        # get the ids of the photos liked and disliked by the current user, then make them lists (values_list itself doesn't return a list object)
        current_user_liked = Like.objects.filter(user_ID=current_user.id).values_list('picture_ID', flat=True)
        current_user_liked = list(current_user_liked)

        current_user_disliked = Dislike.objects.filter(user_ID=current_user.id).values_list('picture_ID', flat=True)
        current_user_disliked = list(current_user_disliked)

        # get the users followed by the current user, make it into a list as well
        current_user_follows = Follow.objects.filter(follower_ID=current_user.id).values_list('followed_ID', flat=True)
        current_user_follows = list(current_user_follows)

        # if the current user has liked less than 5 pictures, set pictures as None value, and list_state as 0
        if len(current_user_liked) < 5:
            context_dict['pictures'] = None
            context_dict['list_state'] = 0

        else:
            # create lists for the recommended pictures
            to_recommend = []
            unique_to_recommend = []

            # get list of users
            users = CustomUser.objects.all()

            # count for how many users that pictures have been added from
            users_added_from = 0

            for us in users:
                # stop after pictures from 30 users has been added
                if users_added_from <= 30:
                    if us != current_user:
                        # get user's liked pictures
                        user_likes = Like.objects.filter(user_ID=us.id).values_list('picture_ID', flat=True)
                        user_likes = list(user_likes)

                        if us.id in current_user_follows:
                            follow_boost = 0.075
                        else:
                            follow_boost = 0

                        # count of how many pictures have been liked by both the current user and user in loop
                        similar = 0
                        for pic in user_likes:
                            if pic in current_user_liked:
                                similar += 1

                        # if the amount of pictures liked by both is at least 15% of the current user's liked pictures
                        # add to 'to_recommend' list as long as the picture is not:
                        # already been liked by the current user, already been disliked by the current user
                        if (((similar / len(current_user_liked)) + follow_boost) > 0.15):
                            for pict in user_likes:
                                if (pict not in current_user_liked) and (pict not in current_user_disliked):
                                    # get the picture object and add it to the list
                                    pic_object = Picture.objects.get(ID=pict)
                                    to_recommend.append(pic_object)
                                    users_added_from += 1

                    # skip to next user if current user in loop is the logged in user
                    else:
                        continue

                # once pictures from 30 users has been added (if it reaches that), stop the loop
                else:
                    break

            # check if list contains pictures
            if to_recommend == []:
                # if 'to_recommend' is empty, pictures is set as None, and list_state as 1
                context_dict['pictures'] = None
                context_dict['list_state'] = 1
            else:
                # remove duplicates
                [unique_to_recommend.append(pic_obj) for pic_obj in to_recommend if pic_obj not in unique_to_recommend]
                # pictures is set as the 'unique_to_recommend' list, and list_state as 2
                context_dict['pictures'] = unique_to_recommend
                context_dict['list_state'] = 2

        return render(request, 'my-feed.html', context=context_dict)


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
    context_dict["title"] = "Login"
    return render(request, "login.html", context=context_dict)


class edit(CreateView):

    model = CustomUser
    form_class = EditForm
    template_name = 'edit-user.html'

    def get(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/home/')
        return super(edit, self).get(form)

    def form_valid(self, form):
        formUser = form.save(commit=False)
        user = CustomUser.objects.get(username=self.request.user.username)
        if formUser.email is not None:
            user.email = formUser.email
        if formUser.profileImage != "userImages/profileImages/default.jpg":
            user.profileImage = formUser.profileImage
        if formUser.city is not None:
            user.city = formUser.city
        if formUser.description is not None:
            user.description = formUser.description
        if formUser.password is not None:
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

    buttonText = "Follow"

    if request.user.is_authenticated:
        try:
            follow = Follow.objects.get(followed_ID=user, follower_ID=request.user)
            buttonText = "Following"
        except ObjectDoesNotExist:
            pass

    pictures = Picture.objects.filter(uploadedBy=user)

    context_dict["profileUser"] = user
    context_dict['pictures'] = pictures
    context_dict["title"] = "Profile"
    context_dict["buttontext"] = buttonText
    return render(request, "profile.html", context=context_dict)


class create(CreateView):
    model = CustomUser
    form_class = PostForm
    template_name = 'add-user.html'

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
