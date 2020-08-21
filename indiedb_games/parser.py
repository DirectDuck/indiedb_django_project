import requests
from bs4 import BeautifulSoup

from .models import Game, GameImage

def parse_status_and_genre(game_container: BeautifulSoup) -> tuple:
    current_span = game_container.find('span', class_='subheading')

    status = current_span.time.text

    time_tag_index = str(current_span).index('</time>')
    end_of_span = str(current_span).index('</span>')
    genre = str(current_span)[time_tag_index + 7:end_of_span].strip()
    
    return status, genre

def parse_image_urls(soup: BeautifulSoup) -> list:
    images = soup.findAll('a', class_='image')
    image_urls = []
    for image in images:
        image_urls.append(image.img['src'])
    return image_urls


def _scrap_new_games(soup: BeautifulSoup) -> dict:
    content = []
    
    titles = soup.findAll('h4')
    game_containers = soup.findAll('div', class_='content')[1:]

    image_urls = parse_image_urls(soup)

    all_game_objects_in_db = Game.objects.all()

    for i in range(len(titles)):
        title = titles[i].text
        try:
            all_game_objects_in_db.get(title=title)
            break
        except:
            status, genre = parse_status_and_genre(game_containers[i])
            content.append({'title': title, 
                            'status': status, 
                            'genre': genre,
                            'image_url': image_urls[i]})

    return content


def _add_game_to_db(game: dict) -> None:
    new_db_game = Game(
        title=game['title'],
        genre=game['genre'],
        status=game['status'])
    new_db_game.save()
    image_db_object = GameImage(game=new_db_game, url=game['image_url'])
    image_db_object.save()


def update_db() -> None:
    link = r'https://www.indiedb.com/games/page/1?sort=id-desc#gamesbrowse'
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    
    scrapped_games = _scrap_new_games(soup)
    
    for game in reversed(scrapped_games):
        _add_game_to_db(game)
