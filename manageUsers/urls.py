from django.urls import path, include
from . import views

app_name = "manageUsers"

urlpatterns = [
    path('myfeed/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='register'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('profile/<ID>/', views.profile, name='profile'),
]