import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'komorebi.settings')
import django

django.setup()
from django.contrib.auth.models import User
from manageImages.models import Picture, Vote, Total
from manageUsers.models import Follow


def populate():
    profiles = [{"model": "komorebi.userprofile", "pk": 34, "fields":
        {"user": 1, "image": "profile_images/meme.jfif", "likes": 0, "dislikes": 0, "name": "Sleep Meme",
         "time": "11:00", "image_id": "user1Sleep Meme"}},
                {"model": "komorebi.userprofile", "pk": 36, "fields":
                    {"user": 2, "image": "profile_images/natural_photo.webp", "likes": 0, "dislikes": 0,
                     "name": "Pretty Scenery", "time": "11:00", "image_id": "user2Pretty Scenery"}},
                {"model": "komorebi.userprofile", "pk": 37, "fields":
                    {"user": 3, "image": "profile_images/sphinx.jpg", "likes": 0, "dislikes": 0, "name": "Sphinx",
                     "time": "11:00",
                     "image_id": "user3Sphinx"}},
                {"model": "komorebi.userprofile", "pk": 38, "fields":
                    {"user": 4, "image": "profile_images/mona_lisa.jpg", "likes": 0, "dislikes": 0,
                     "name": "Mona Lisa", "time": "11:00", "image_id": "user4Mona Lisa"}},
                {"model": "komorebi.userprofile", "pk": 39, "fields":
                    {"user": 5, "image": "profile_images/ghandi.jfif", "likes": 0, "dislikes": 0, "name": "Ghandi",
                     "time": "11:00", "image_id": "user5Ghandi"}}]
    for profile in profiles:
        userprofile = profile["fields"]
        add_userProfile(userprofile["user"], userprofile["image"], userprofile["likes"], userprofile["dislikes"],
                        userprofile["name"], userprofile["image_id"], userprofile["time"])


def add_userProfile(user_id, image, likes, dislikes, name, image_id, time):
    credentials = {
        'username': 'user' + str(user_id),
        'password': 'user' + str(user_id)}
    user = User.objects.create_user(**credentials)
    total = Total(user=user)
    total.dislikes = 0
    total.likes = 0
    total.save()
    p = Picture.objects.get_or_create(user=user, image=image, likes=likes, dislikes=dislikes, name=name, time=time,
                                      image_id=image_id)[0]
    p.save()


if __name__ == '__main__':
    print('Starting komorebi population script...')
    populate()
