import uuid

from django.db import models

# Create your models here.
from komorebi.settings import MEDIA_URL


# model for voting pictures
class Vote(models.Model):
    vote_id = models.CharField(max_length=128, primary_key=True, unique=True)
    vote_type = models.CharField(max_length=128, default='')


class Picture(models.Model):
    ID = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='userImages/', null=False, blank=False)
    name = models.CharField(max_length=100)
    url = models.URLField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    # TODO - add 'Uploaded by' foreign key

    def __str__(self):
        return "ID: " + str(self.ID) + " name: " + self.name
