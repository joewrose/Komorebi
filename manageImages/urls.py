from django.urls import path, include
from . import views

app_name = "manageImages"

urlpatterns = [
    path('', views.index, name='index'),
    path('<ID>/', views.closeup, name='closeup'),

]