from django.db import models

# Create your models here.
from komorebi.settings import MEDIA_URL


class Picture(models.Model):
    ID = models.IntegerField
    image = models.ImageField(upload_to='userImages', null=False, blank=False)
    name = models.CharField(max_length=100)
    url = models.URLField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField()
    # TODO - add 'Uploaded by' foreign key

    def __str__(self):
        return "ID: " + self.ID + " name: " + self.name