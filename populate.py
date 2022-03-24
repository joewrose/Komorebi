import os
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django

django.setup()
from django.contrib.auth.models import User
from manageImages.models import Picture, Like, Dislike
from manageUsers.models import Follow
from random import randint
import os
import datetime


from django.contrib.auth import get_user_model
User = get_user_model()
directory = os.fsencode('media/userImages/')

paths = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    paths.append(filename)

namesFile = open('populateFirstNames.txt','r')
usernamesFile = open('populateUsernames.txt','r')

usernames = []
firstnames = []
lastnames = []

for line in usernamesFile:
    usernames.append(line)

for line in namesFile:
    firstnames.append(line.split()[0])
    lastnames.append(line.split()[1])

def populate():
    for i in range(199):
        addUser(usernames[i],firstnames[i],lastnames[i])
    for i in range(len(paths)):
        addPicture('Image' + str(i), 'userImages/' + paths[i])


def addUser(username, firstname, lastname):


    u = User.objects.get_or_create(username=username,email="testEmail@test.com",password=uuid.uuid4())

def addPicture(name, image):
    user = User.objects.get(username=usernames[2])
    picture_ID = uuid.uuid4()
    p = Picture.objects.get_or_create(ID=picture_ID,image=image,name=name,uploadedBy=user,time=datetime.datetime.now())[0]
    amountLikes = randint(0,30)
    amountDislikes = randint(0, 30)

    for i in range(amountLikes):
        l = Like.objects.get_or_create(user_ID=User.objects.get(username = usernames[i]), picture_ID=Picture.objects.get(ID=picture_ID))

    for i in range(amountDislikes):
        d = Dislike.objects.get_or_create(user_ID=User.objects.get(username = usernames[i]), picture_ID=Picture.objects.get(ID=picture_ID))

    p.save()


if __name__ == '__main__':
    print('Starting komorebi population script...')
    populate()