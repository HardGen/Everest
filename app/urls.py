from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
    path('', main, name='main'),
    path('players/', players, name='players'),
    path('workouts/', workouts, name='workouts'),
    path('/games', games, name='games'),
]
