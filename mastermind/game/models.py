from django.contrib.postgres.fields import ArrayField
from django.db import models


COLORS = (
    ('R', 'RED'),
    ('B', 'BLUE'),
    ('G', 'GREEN'),
    ('Y', 'YELLOW'),
)

COLORS_REVERSE = {v: k for k, v in COLORS}

AVAILABLE_ROUNDS = [12, 10, 8, 6]


class Game(models.Model):
    # Fields
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), size=4)
    n_rounds = models.IntegerField()
    won = models.BooleanField(default=False)

    # Functions
    @property
    def round_count(self):
        return self.rounds.all().count()

    @property
    def ended(self):
        return self.won or self.round_count == self.n_rounds


class Round(models.Model):
    # Relations
    game = models.ForeignKey(Game,
                             related_name="rounds",
                             verbose_name=u"Game", on_delete=models.CASCADE)

    # Fields
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), size=4)
    black_pegs = models.IntegerField()
    white_pegs = models.IntegerField()
