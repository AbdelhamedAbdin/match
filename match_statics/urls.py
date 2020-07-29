from . import views
from django.urls import path

app_name = 'match_statics'

urlpatterns = [
    path('player_statics/<int:pk>/', views.player_statics, name='player_statics'),
]
