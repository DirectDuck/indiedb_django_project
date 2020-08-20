import requests
from bs4 import BeautifulSoup

from .models import Game

link = r'https://www.indiedb.com/games/page/1?sort=id-desc#gamesbrowse'

def _scrap_page(soup: BeautifulSoup) -> dict:
    content = []
    titles = soup.findAll('h4')
    information = soup.findAll('div', class_='content')[1:]
    
    for i in range(len(titles)):
        current_span = information[i].find('span', class_='subheading')
        
        status = current_span.time.text
        
        time_tag_index = str(current_span).index('</time>')
        end_of_span = str(current_span).index('</span>')
        genre = str(current_span)[time_tag_index+7:end_of_span].strip()
        
        content.append({'title': titles[i].text, 'status': status, 'genre': genre})
    
    return content

def _add_game_to_db(game):
    new_db_object = Game(
        title=game['title'],
        genre=game['genre'],
        status=game['status'])
    new_db_object.save()

def update_db() -> None:
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    scrapped_games = _scrap_page(soup)
    all_game_objects_in_db = Game.objects.all()
    for game in scrapped_games:
        try:
            all_game_objects_in_db.get(title=game['title'])
        except:
            _add_game_to_db(game)

