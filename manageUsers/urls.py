from django.urls import path, include
from . import views

app_name = "manageUsers"

urlpatterns = [
    path('myfeed/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]