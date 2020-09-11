

# Indiedb Django Project

Welcome to my test Django project. It was created just to showcase some of my skills.

## Technologies used in the project

### Primary:
 - Django
 - Postgresql (psycopg2)
 - BeautifulSoup4 + requests

### Secondary:
- django-crontab
- Celery + Redis (now replaced with django-crontab)
- django-environ
- Docker

### Django topics covered

- Pagination
- Function-based views
- Models (including OneToOneField, slugs)
- Django templates (As simple as possible)
- Forms

## TODO

1. Users
>Initially, the project was not supposed to have anything related to users and authentication / authorization systems, but in the future this may become part of the project.

2. ~~Dockerization of project~~

3. Deploying application

4. Making it look pretty with bootstrap

## How to run this on your machine
Important Note: It is impossible to run the project on Windows since django-crontab only works with Linux-like operating systems.

Third-party application to install:

- Docker version 19.03.12
- docker-compose version 1.26.2
- PostgreSQL 11.9

>You might try running with different versions, but it's not guaranteed to work.


1. Enter `git clone https://github.com/DirectDuck/indiedb_django_project.git` in terminal
2. Go inside project folder (`cd indiedb_django_project`)
3. From terminal, run `docker-compose --env-file ./config/.env.example up -d --build` 
4. From terminal, run `docker-compose exec web python manage.py migrate` and proceed to `http://127.0.0.1:8000/`

> If page doesn't load then type `docker-compose logs`. If you can't manage to resolve the problem, create an issue.

