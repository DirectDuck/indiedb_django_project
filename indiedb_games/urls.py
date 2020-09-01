from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='list'),
    path('update/', views.update_game_list, name='update'),
    path('clear_db/', views.clear_db, name='clear')
]
