from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render

from .models import Game
from .forms import SearchForm
from . import parser


def game_list(request):
    form = SearchForm()
    if 'genre' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            objects = Game.objects.filter(genre=genre)
    else:
        objects = Game.objects.all()
    return render(
        request, 
        'indiedb_games/game_list.html', 
        {'games': objects,
         'form': form}
    )

def update_game_list(request):
    parser.update_db()
    return redirect('list')