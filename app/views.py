from django.http import HttpRequest
from .models import *
from django.shortcuts import render

# Create your views here.
def main(request: HttpRequest):
    return render(request, 'app/base.html')



def players(request: HttpRequest):
    return render(request, 'app/players.html')



def workouts(request: HttpRequest):
    return render(request, 'app/workouts.html')



def games(request: HttpRequest):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'app/games.html', context=context)

