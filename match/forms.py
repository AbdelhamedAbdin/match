from django import forms
from .models import PlayerName, PlayerBase, PlayerBaseData, PlayerMain


PLAYERS = PlayerName.objects.values_list('name', 'name')


class PlayerForm(forms.ModelForm):
    box = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PLAYERS,
    )

    class Meta:
        model = PlayerBase
        fields = ['box']


PLAYER_BASE_DATA = PlayerBaseData.objects.values_list('name', 'name')


class PlayerMainForm(forms.ModelForm):
    box = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PLAYER_BASE_DATA,
    )

    class Meta:
        model = PlayerMain
        fields = ['box']
