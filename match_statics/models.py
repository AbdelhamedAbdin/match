from django.db import models
from match.models import PlayerName
from django.db.models.signals import post_save


class Statistics(models.Model):
    # main = models.ForeignKey(PlayerName, on_delete=models.CASCADE, related_name='static_field')
    main = models.OneToOneField(PlayerName, on_delete=models.CASCADE)
    short_pass = models.PositiveIntegerField(default=0)
    long_pass = models.PositiveIntegerField(default=0)

    def __int__(self):
        return self.main.pk

    # danger_pass = models.PositiveIntegerField(default=0)
    # not_danger_pass = models.PositiveIntegerField(default=0)
    # cross = models.PositiveIntegerField(default=0)
    # flat = models.PositiveIntegerField(default=0)
    # foul_goal = models.PositiveIntegerField(default=0)
    # foul_try = models.PositiveIntegerField(default=0)
    # foul_none = models.PositiveIntegerField(default=0)
    # corner_goal = models.PositiveIntegerField(default=0)
    # corner_try = models.PositiveIntegerField(default=0)
    # corner_none = models.PositiveIntegerField(default=0)
    # tackl_ok = models.PositiveIntegerField(default=0)
    # tackl_none = models.PositiveIntegerField(default=0)
    # dribble_try = models.PositiveIntegerField(default=0)
    # dribble_none = models.PositiveIntegerField(default=0)
    # g_keeper_safe = models.PositiveIntegerField(default=0)
    # g_keeper_danger = models.PositiveIntegerField(default=0)
    # block_good = models.PositiveIntegerField(default=0)
    # block_bad = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.main


def create_player_name(sender, **kwargs):
    if kwargs['created']:
        user_profile = Statistics.objects.create(main=kwargs['instance'])


post_save.connect(receiver=create_player_name, sender=PlayerName)
