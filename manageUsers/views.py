import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from manageImages.models import Picture
from django.db.models import Count



# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm, NewUserForm
from manageImages.models import Picture

def index(request):
    return HttpResponse("Welcome to the manageUsers Index page!")

def myfeed(request): 
    if not request.user.is_authenticated:
        redirect('/home')
        
    else:
        current_user = request.user
        current_user_liked = Likes.objects.values('picture_ID').filter(user_ID = current_user)
        current_user_disliked = Dislikes.objects.values('picture_ID').filter(user_ID = current_user)
        
        # if the current user has liked less than 5 pictures, return None value
        if len(current_user_liked) < 5:
            context_dict = {'myfeed_pictures': None}

        else:
            # create list for the recommended pictures
            to_recommend = list()
            # get list of users
            users = CustomUser.objects.all()
            users_checked = 0

            for us in users:
                # stop after pictures from 30 users has been added
                if users_checked <= 30:
                    if us != current_user:
                        user_likes = Likes.object.values('picture_ID').filter(user_ID = us)
                        if len(user_likes) > 5:
                            similar = 0
                            # get the amount of pictures that have been liked by both
                            for pic in user_likes:
                                if pic is in current_user_liked:
                                    similar += 1
                            # if the amount of pictures liked by both is a least a third of the current user's liked pictures
                            # add to 'to_recommend' list as long as the picture is not: 
                            # already in 'to_recommend', already been liked by the current user, already been disliked by the current user
                            if similar > (len(current_user_liked)/3):
                                for pict in current_user_liked:
                                    if pict not in to_recommend && pict not in current_user_liked && pict not in current_user_disliked:
                                        to_recommend.append(pict)
                                        users_checked += 1
                    else:
                        continue
                else:
                    break

            # check if list contains pictures
            if to_recommend == []:
                context_dict = {'myfeed_pictures': "empty"}
            else:
                context_dict = {'myfeed_pictures': to_recommend}

        return render(request, 'myfeed.html', context=context_dict)

def dashboard(request):
    return HttpResponse("Welcome to the manageUsers Dashboard page!")

def home(request):
    current_user = request.user
    context_dict = {}

    if request.user.is_authenticated:
        pictures = Picture.objects.filter(uploaded_by != current_user).annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]
    else:
        pictures = Picture.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]
    
    for image in pictures:
        print(image)

    context_dict["pictures"] = pictures
    
    return render(request, "home.html", context_dict)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("myfeed/")
        else:
            messages.success(request, "There was an error logging you in, try again")
            return redirect("login")

    return render(request, "login.html")

def edit(request):
    return HttpResponse("Welcome to the manageUsers Edit page!")

def profile(request):
    return HttpResponse("Welcome to the manageUsers Profile page!")

def create(request):

    context_dict = {}

    pictures = Picture.objects.annotate(num_likes=Count('likes'))[:6]

    context_dict["pictures"] = pictures

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    context_dict["register_form"] = form

    return render(request, "addUser.html", context=context_dict)
