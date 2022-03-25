from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "manageUsers"

urlpatterns = [
    path('home/', views.index, name='home'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', views.login, name='login'),
    path('create/', views.create.as_view(), name='create'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('profile/<username>/', views.profile, name='profile'),
]
