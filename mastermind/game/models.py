from django.contrib.postgres.fields import ArrayField
from django.db import models


COLORS = (
    ('R', 'RED'),
    ('B', 'BLUE'),
    ('G', 'GREEN'),
    ('Y', 'YELLOW'),
)


class Game(models.Model):
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), max_length=4)
    ended = models.BooleanField(default=False)
    won = models.BooleanField(default=False)


class Round(models.Model):
    group = models.ForeignKey(Game, on_delete=models.CASCADE)
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), max_length=4)
    black_pegs = models.IntegerField(null=True)
    white_pegs = models.IntegerField(null=True)
