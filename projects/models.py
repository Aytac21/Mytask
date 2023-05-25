from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.FloatField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, blank=True)
    rank = models.FloatField()

    def __str__(self):
        return self.name
