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

directory = os.fsencode('populateImages/')

paths = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    paths.append(filename)


def populate():
    for i in range(len(paths)):
        addPicture('Image' + str(i), 'populateImages/' + paths[i])


def addPicture(image, name):
    user = User.objects.get()
    p = Picture.objects.get_or_create(ID=uuid.uuid4(),image=image,name=name,uploadedBy=user,time=datetime.datetime.now())[0]
    p.save()


if __name__ == '__main__':
    print('Starting komorebi population script...')
    populate()