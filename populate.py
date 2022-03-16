import os
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django

django.setup()
from django.contrib.auth.models import User
from manageImages.models import Picture, Vote
from manageUsers.models import Follow
import os
import datetime

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
    u = User.objects.get_or_create(username=username,first_name=firstname,last_name=lastname,password=uuid.uuid4())

def addPicture(name, image):
    user = User.objects.get(first_name='Holden')
    p = Picture.objects.get_or_create(ID=uuid.uuid4(),image=image,name=name,uploadedBy=user,time=datetime.datetime.now())[0]
    p.save()


if __name__ == '__main__':
    print('Starting komorebi population script...')
    populate()