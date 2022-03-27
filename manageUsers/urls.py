from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "manageUsers"

urlpatterns = [
    path('home/', views.index, name='home'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', views.login, name='login'),
    path('create/', views.create.as_view(), name='create'),
    path('edit/', views.edit.as_view(), name='edit'),
    path('profile/<username>/', views.profile, name='profile'),
    path('follow/', views.follow.as_view(), name='follow'),
]
