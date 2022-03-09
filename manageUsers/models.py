from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Follow(models.Model):
    follower_ID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)_follower')
    followed_ID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)_followed')
    ID = models.UniqueConstraint(fields=['follower_ID', 'followed_ID'], name='Composite_Key')

    def __str__(self):
        return "User with ID " + str(self.follower_ID) + " followed user with ID" + str(self.followed_ID)
