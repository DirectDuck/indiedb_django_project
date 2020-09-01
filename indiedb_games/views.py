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

    genre_additional_url = services.generate_additional_genre_url(genre)

    objects = services.paginate_objects(request, objects)

    return render(
        request,
        'indiedb_games/game_list.html',
        {'games': objects,
         'form': form,
         'genre_additional_url': genre_additional_url}
    )


def update_game_list(request):
    parser.update_db()
    return redirect('list')


def clear_db(request):
    for game in Game.objects.all():
        game.delete()
    return redirect('list')
