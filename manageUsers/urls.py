from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "manageUsers"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('profile/<ID>/', views.profile, name='profile'),
    path('login', views.login, name='login'),
]
