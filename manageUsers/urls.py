from django.urls import path, include
from . import views

app_name = "manageUsers"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='register'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('profile/<ID>/', views.profile, name='profile'),
]
