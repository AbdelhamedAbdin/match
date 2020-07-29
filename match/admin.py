from django.contrib import admin
from .models import Match, PlayerName, PlayerBaseData, Main, Substitution, PlayerMain

admin.site.register(Match)
admin.site.register(PlayerName)
admin.site.register(PlayerBaseData)
admin.site.register(Main)
admin.site.register(Substitution)
admin.site.register(PlayerMain)
