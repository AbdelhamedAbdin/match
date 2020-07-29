from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Match, PlayerName, PlayerBaseData, Main, Substitution
from .forms import PlayerForm, PlayerMainForm
from match_statics.models import Statistics


class MatchListView(ListView):
    template_name = 'match/matchs.html'
    model = Match
    context_object_name = 'all_matches'


def match_details(request, pk):
    template_name = 'match/match_details.html'
    match_pk = get_object_or_404(Match, id=pk)
    player_name = PlayerName.objects.all()

    if request.method == 'POST':
        objects = request.POST.getlist('box')
        for obj in objects:
            data = PlayerBaseData.objects.get_or_create(name=obj)
        return redirect('match:player_main')

    form = PlayerForm()
    context = {'match_pk': match_pk, 'player_name': player_name,
               'form': form}
    return render(request, template_name, context)


def choose_player_main(request):
    template_name = 'match/player_main.html'
    player_data = PlayerBaseData.objects.values('name')
    player_main = Main.objects.all()
    # request to save main and sub players in custom page
    if request.method == 'POST':
        objects = request.POST.getlist('box')
        for key in player_data:
            if key['name'] in objects:
                Main.objects.get_or_create(team=key['name'])
            else:
                Substitution.objects.get_or_create(team=key['name'])
        return redirect('match:players')

    # the players who will choice between theme (GET method)
    form = PlayerMainForm()
    context = {'form': form, 'player_data': player_data, 'player_main': player_main}
    return render(request, template_name, context)


def players_view(request):
    player_main = Main.objects.all()
    player_sub = Substitution.objects.all()
    context = {'player_main': player_main, 'player_sub': player_sub}
    return render(request, 'match/players_view.html', context)
