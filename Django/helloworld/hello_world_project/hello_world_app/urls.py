# hello_world_app/urls.py
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]