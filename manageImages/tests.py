from django.test import TestCase
from django.urls import reverse

from manageImages.forms import ImageForm
import os
import uuid

from manageUsers.models import CustomUser
from populate import usernames

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django
from django.core.files.uploadedfile import SimpleUploadedFile
django.setup()
from manageImages.models import Picture, Like, Dislike
from random import randint
import os
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()
directory = os.fsencode('media/userImages/')

paths = []


class ImageFormTests(TestCase):

    # Check that the form will reject an invalid email
    def test_invalid_file(self):
        video = SimpleUploadedFile("file.mp4", bytes("file_content", encoding='utf-8'), content_type="video/mp4")

        response = self.client.post(reverse('manageImages:addimage'), {'name':'testImage;=','image': video})

        self.assertTrue("Upload a valid image." in response.content.decode())

    # Check that the form will reject a form with an empty name
    def test_empty_name(self):
        form = ImageForm(
            data={"name": "", "image": "Testfile.png"})

        self.assertTrue("This field is required." in str(form.errors))

    # Tests that we can add a picture to the database successfully
    def test_create_picture(self):
        populate()
        p = Picture.objects.filter(name="TestPicture")
        self.assertEqual(len(p), 1)
        self.assertEqual(str(p[0].image),"picture.png")

    # Check that the form will accept a valid form
    def test_complete_form(self):
        populate()

        # small_gif data from StackOverflow thread:
        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')

        user = CustomUser.objects.get(username=usernames[2])
        self.client.force_login(user)

        response = self.client.post(reverse('manageImages:addimage'), {'name':'testImage','image': image})

        self.assertTrue("Upload a valid image." not in response.content.decode() and "This field is required." not in response.content.decode())


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    paths.append(filename)

namesFile = open('populateFirstNames.txt', 'r')
usernamesFile = open('populateUsernames.txt', 'r')

usernames = []
firstnames = []
lastnames = []

for line in usernamesFile:
    usernames.append(line)

for line in namesFile:
    firstnames.append(line.split()[0])
    lastnames.append(line.split()[1])


def populate():
    addUser("TestUser")
    for i in range(199):
        addUser(usernames[i])
    addPicture("TestPicture", "picture.png")
    for i in range(len(paths)):
        addPicture('Image' + str(i), 'userImages/' + paths[i])


def addUser(username):
    u = CustomUser.objects.get_or_create(username=username, email="testEmail@test.com", password=uuid.uuid4())

def addPicture(name, image):
    user = CustomUser.objects.get(username=usernames[2])
    picture_ID = uuid.uuid4()
    p = Picture.objects.get_or_create(ID=picture_ID, image=image, name=name, uploadedBy=user, time=datetime.datetime.now())[0]
    amountLikes = randint(0, 30)
    amountDislikes = randint(0, 30)

    for i in range(amountLikes):
        l = Like.objects.get_or_create(user_ID=User.objects.get(username=usernames[i]),
                                       picture_ID=Picture.objects.get(ID=picture_ID))

    for i in range(amountDislikes):
        d = Dislike.objects.get_or_create(user_ID=User.objects.get(username=usernames[i]),
                                          picture_ID=Picture.objects.get(ID=picture_ID))

    p.save()
