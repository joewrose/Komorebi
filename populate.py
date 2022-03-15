import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django

django.setup()
from django.contrib.auth.models import User
from manageImages.models import Picture, Vote
from manageUsers.models import Follow


def populate():
    pictures = [{"model": "komorebi.Picture", "pk": 34, "fields":
        {"image": "userImages/meme.jfif", "likes": 0, "dislikes": 0, "name": "Sleep Meme",
         }},
                {"model": "komorebi.Picture", "pk": 36, "fields":
                    {"image": "userImages/natural_photo.webp", "likes": 0, "dislikes": 0,
                     "name": "Pretty Scenery", }},
                {"model": "komorebi.Picture", "pk": 37, "fields":
                    {"image": "userImages/sphinx.jpg", "likes": 0, "dislikes": 0, "name": "Sphinx",

                     }},
                {"model": "komorebi.Picture", "pk": 38, "fields":
                    {"image": "userImages/mona_lisa.jpg", "likes": 0, "dislikes": 0,
                     "name": "Mona Lisa", "time": "11:00"}},
                {"model": "komorebi.Picture", "pk": 39, "fields":
                    {"image": "userImages/ghandi.jfif", "likes": 0, "dislikes": 0, "name": "Ghandi",
                     }}]
    for picture in pictures:
        userpicture = picture["fields"]
        add_userPicture(userpicture["image"], userpicture["likes"], userpicture["dislikes"],
                        userpicture["name"])


def add_userPicture(user_Id, image, likes, dislikes, name):
    credentials = {
        'username': 'user' + str(user_Id),
        'password': 'user' + str(user_Id)}
    # username = User.objects.create_user(**credentials)
    p = Picture.objects.get_or_create(image=image, likes=likes, dislikes=dislikes, name=name)[0]

    p.save()


if __name__ == '__main__':
    print('Starting komorebi population script...')
    populate()
