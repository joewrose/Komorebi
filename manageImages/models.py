import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from komorebi.settings import MEDIA_URL


class Picture(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4())
    image = models.ImageField(upload_to='userImages/', null=False, blank=False)
    name = models.CharField(max_length=100)
    url = models.URLField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    # TODO - add 'Uploaded by' foreign key

    def __str__(self):
        return "ID: " + str(self.ID) + " name: " + self.name


# Model for voting pictures, uses a composite primary key made from the userID and pictureID, this works as the
# user cannot both like and dislike an image. 'type' is a single letter, either 'L' or 'D'.
class Vote(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_ID = models.ForeignKey(Picture, on_delete=models.CASCADE)
    ID = models.UniqueConstraint(fields=['user_ID', 'picture_ID'], name='Composite_Key')
    type = models.CharField(max_length=1, default='')

    def __str__(self):
        return "User with ID " + str(self.user_ID) + " voted " + self.vote_type + " for photo with ID " + str(
            self.picture_ID)


class Follow(models.Model):
    follower_ID = models.ForeignKey(User, on_delete=models.CASCADE)

    ID = models.UniqueConstraint(fields=['follower_ID', 'followed_ID'], name='Composite_Key')

    def __str__(self):
        return "User with ID " + str(self.follower_ID) + " followed user with ID" + str(self.followed_ID)
