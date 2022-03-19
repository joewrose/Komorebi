from django.urls import path, include
from . import views

app_name = "manageImages"

urlpatterns = [
    path('closeup/<ID>/', views.closeup, name='closeup'),
    path('addImage/', views.addimage, name='addimage'),
    path('like_picture/', views.LikePictureView.as_view(), name='like_picture'),
]