from django.test import TestCase
from manageUsers.forms import PostForm, EditForm
import os
import uuid

from manageUsers.models import CustomUser
from populate import usernames

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django

django.setup()
from django.contrib.auth.models import User
from manageImages.models import Picture, Like, Dislike
from random import randint
import os
import datetime


from django.contrib.auth import get_user_model
User = get_user_model()
directory = os.fsencode('media/userImages/')

paths = []



class PostFormTests(TestCase):

    # Check that the form will reject an invalid email
    def test_invalid_email(self):
        form = PostForm(
            data={"username": "Kingarth", "email": "invalidemail", "city": "Glasgow, UK", "description": "Chillin'",
                  "password": "Summer2022"})

        self.assertTrue("Enter a valid email address." in str(form.errors))

    # Check that the form will reject a form with an empty required field
    def test_missing_required_field(self):
        form = PostForm(
            data={"username": "Kingarth", "email": "joewallacerose@hotmail.com", "city": "Glasgow, UK",
                  "description": "",
                  "password": "Summer2022"})

        self.assertTrue("This field is required." in str(form.errors))

    # Check that the form will accept a valid form
    def test_valid_form(self):
        form = PostForm(
            data={"username": "Kingarth", "email": "joewallacerose@hotmail.com", "city": "Glasgow, UK",
                  "description": "Chillin'",
                  "password": "Summer2022"})

        self.assertTrue(str(form.errors) == "")

    def test_create_user(self):
        populate()
        u = User.objects.filter(username="TestUser")
        self.assertEqual(len(u),1)

class EditFormTests(TestCase):

    # Check that the form will reject an invalid email
    def test_invalid_email(self):
        form = EditForm(
            data={"email": "invalidemail", "city": "Glasgow, UK", "description": "Chillin'",
                  "password": "Summer2022"})

        self.assertTrue("Enter a valid email address." in str(form.errors))

    # Check that the form will accept an empty form
    def test_empty_form(self):
        form = EditForm(
            data={"email": "", "city": "",
                  "description": "",
                  "password": ""})

        self.assertTrue(str(form.errors) == "")

    # Check that the form will accept a vald form
    def test_valid_form(self):
        form = EditForm(
            data={"email": "joewallacerose@hotmail.com", "city": "Glasgow, UK",
                  "description": "Chillin'",
                  "password": "Summer2022"})

        self.assertTrue(str(form.errors) == "")


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
    for i in range(len(paths)):
        addPicture('Image' + str(i), 'userImages/' + paths[i])


def addUser(username):
    u = CustomUser.objects.get_or_create(username=username,email="testEmail@test.com",password=uuid.uuid4())

def addPicture(name, image):
    user = CustomUser.objects.get(username="TestUser")
    picture_ID = uuid.uuid4()
    p = Picture.objects.get_or_create(ID=picture_ID,image=image,name=name,uploadedBy=user,time=datetime.datetime.now())[0]
    amountLikes = randint(0,30)
    amountDislikes = randint(0, 30)

    for i in range(amountLikes):
        l = Like.objects.get_or_create(user_ID=User.objects.get(username = usernames[i]), picture_ID=Picture.objects.get(ID=picture_ID))

    for i in range(amountDislikes):
        d = Dislike.objects.get_or_create(user_ID=User.objects.get(username = usernames[i]), picture_ID=Picture.objects.get(ID=picture_ID))

    p.save()

