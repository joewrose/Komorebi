from django.urls import path, include
from . import views

app_name = "manageUsers"

urlpatterns = [
    path('about/', views.about, name='home'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('profile/<ID>/', views.profile, name='profile'),
]
