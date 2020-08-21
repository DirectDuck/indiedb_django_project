from django.shortcuts import redirect, render

from .models import Game
from .forms import SearchForm
from . import parser
from . import services


def game_list(request):
    form = SearchForm()
    genre = ''
    if 'genre' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            genre = form.cleaned_data['genre'].lower().capitalize()
            objects = Game.objects.filter(genre=genre)
    else:
        objects = Game.objects.all()

    if genre: genre = f'&genre={genre}'

    objects, page = services.paginate_objects(request, objects)

    return render(
        request, 
        'indiedb_games/game_list.html', 
        {'games': objects,
         'form': form,
         'page': page,
         'genre': genre}
    )

def update_game_list(request):
    parser.update_db()
    return redirect('list')