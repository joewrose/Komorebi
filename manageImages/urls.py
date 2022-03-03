from django.urls import path
from . import views

app_name = "rango"

urlpatterns = [
    path('', views.index, name='index'),
]