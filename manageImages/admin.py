from django.contrib import admin

from manageImages.models import Picture
from manageImages.models import Vote

admin.site.register(Picture)
admin.site.register(Vote)