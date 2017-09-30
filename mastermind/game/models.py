from django.contrib.postgres.fields import ArrayField
from django.db import models


COLORS = (
    ('R', 'RED'),
    ('B', 'BLUE'),
    ('G', 'GREEN'),
    ('Y', 'YELLOW'),
)


class Game(models.Model):
    # Fields
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), size=4)
    ended = models.BooleanField(default=False)
    won = models.BooleanField(default=False)

    # Functions
    @property
    def round_count(self):
        return self.rounds.all().count()


class Round(models.Model):
    # Relations
    game = models.ForeignKey(Game,
                             related_name="rounds",
                             verbose_name=u"Game", on_delete=models.CASCADE)

    # Fields
    code = ArrayField(models.CharField(max_length=1, choices=COLORS), size=4)
    black_pegs = models.IntegerField(null=True)
    white_pegs = models.IntegerField(null=True)
