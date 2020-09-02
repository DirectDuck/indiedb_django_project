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

### Django topics covered

- Pagination
- Function-based views
- Models (including OneToOneField, slugs)
- Django templates (As simple as possible)
- Forms

### TODO

1. Users
>Initially, the project was not supposed to have anything related to users and authentication / authorization systems, but in the future this may become part of the project.

2. Dockerization of project

3. Deploying application

### How to run this on your machine
Important Note: It is impossible to run the project on Windows since django-crontab only works with Linux-like operating systems.

1. Enter `git clone https://github.com/DirectDuck/indiedb_django_project.git` in terminal
2. Go inside project folder (`cd indiedb_django_project`)
3. Install dependencies from requirements.txt via `pip install -r requirements.txt` (It is recommended to use a virtual environment)
4. Create **Postgresql** database for this project
5. In `config/` folder create `.env` file and fill it with following variables:  
	1. DEBUG
	>Either "on" or "off"

	2. INDIEDB_PROJECT_SECRET_KEY
	3. INDIEDB_PROJECT_DATABASE_NAME
	4. INDIEDB_PROJECT_DATABASE_USERNAME
	5. INDIEDB_PROJECT_DATABASE_PASSWORD
	6. INDIEDB_PROJECT_DATABASE_HOST
	7. INDIEDB_PROJECT_DATABASE_PORT
6. From terminal, run `python manage.py migrate` 
7. From terminal, run `python manage.py runserver` and proceed to `http://127.0.0.1:8000/`
