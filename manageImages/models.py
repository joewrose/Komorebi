import uuid

from django.contrib.auth.models import User
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from manageUsers.models import CustomUser

# Create your models here.
from komorebi.settings import MEDIA_URL


class Picture(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4())
    image = models.ImageField(upload_to='userImages/', null=False, blank=False)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(500, 500)],
                               format='JPEG',
                               options={'quality': 60})
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    uploadedBy = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "name: " + self.name + " ID: " + str(self.ID)


# Model for voting pictures, uses a composite primary key made from the userID and pictureID, this works as the
# user cannot both like and dislike an image.
class Like(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    picture_ID = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='likes')
    ID = models.UniqueConstraint(fields=['user_ID', 'picture_ID'], name='Composite_Key')

    def __str__(self):
        return "User with ID " + str(self.user_ID) + " liked photo with ID " + str(self.picture_ID)


class Dislike(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dislikes')
    picture_ID = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='dislikes')
    ID = models.UniqueConstraint(fields=['user_ID', 'picture_ID'], name='Composite_Key')

    def __str__(self):
        return "User with ID " + str(self.user_ID) + " liked photo with ID " + str(self.picture_ID)
