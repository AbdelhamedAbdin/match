from . import views
from django.urls import path

app_name = 'match'

urlpatterns = [
    path('', views.MatchListView.as_view(), name='home'),
    path('details/<int:pk>/', views.match_details, name='match_details'),
    path('player_main/', views.choose_player_main, name='player_main'),
    path('players/', views.players_view, name='players'),
]
