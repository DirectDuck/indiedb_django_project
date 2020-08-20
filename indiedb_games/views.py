from django.views.generic import ListView, DetailView

from .models import Game

class GamesList(ListView):
    model = Game
    template_name = 'list.html'

GamesListView = GamesList.as_view()