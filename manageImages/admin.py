from django.contrib import admin

from manageImages.models import Picture
from manageImages.models import Like
from manageImages.models import Dislike

admin.site.register(Picture)
admin.site.register(Like)
admin.site.register(Dislike)
