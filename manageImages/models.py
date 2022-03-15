import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from komorebi.settings import MEDIA_URL


class Picture(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4())
    image = models.ImageField(upload_to='userImages/', null=False, blank=False)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    uploadedBy = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "ID: " + str(self.ID) + " name: " + self.name


# Model for voting pictures, uses a composite primary key made from the userID and pictureID, this works as the
# user cannot both like and dislike an image.
class Vote(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_ID = models.ForeignKey(Picture, on_delete=models.CASCADE)
    ID = models.UniqueConstraint(fields=['user_ID', 'picture_ID'], name='Composite_Key')
    like = models.BooleanField(default=True)

    def __str__(self):
        return "User with ID " + str(self.user_ID) + " voted " + self.vote_type + " for photo with ID " + str(
            self.picture_ID)


