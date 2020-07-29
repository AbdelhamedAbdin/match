from django.db import models
from django.urls import reverse


class Match(models.Model):
    match = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.match

    def get_absolute_url(self):
        return reverse('match:match_details', self.pk)


class PlayerName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlayerBase(models.Model):
    box = models.CharField(max_length=255)

    def __str__(self):
        return self.box


class PlayerBaseData(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlayerMain(models.Model):
    box = models.CharField(max_length=255)

    def __str__(self):
        return self.box


class Main(models.Model):
    team = models.CharField(max_length=255)

    def __str__(self):
        return self.team

    def get_id(self):
        return self.pk


class Substitution(models.Model):
    team = models.CharField(max_length=255)

    def __str__(self):
        return self.team
