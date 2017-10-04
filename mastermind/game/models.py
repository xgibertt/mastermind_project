from django.contrib.postgres.fields import ArrayField
from django.db import models
from collections import Counter


COLORS = (
    ('R', 'RED'),
    ('B', 'BLUE'),
    ('G', 'GREEN'),
    ('Y', 'YELLOW'),
)

COLORS_VALUES = {v: k for k, v in COLORS}

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

    # Functions
    @property
    def ended(self):
        return self.game.ended

    @property
    def won(self):
        return self.game.won

    def save(self, *args, **kwargs):
        if self.code == self.game.code:
            self.game.won = True
            self.game.save()

        self.black_pegs, self.white_pegs = self._calculate_pegs(self.game.code, self.code)

        super(Round, self).save(*args, **kwargs)

    def _calculate_pegs(self, game_code, round_code):
        black_pegs = white_pegs = 0

        if game_code == round_code:
            black_pegs = 4
        else:
            game_miss = Counter()
            round_miss = Counter()

            for i, val in enumerate(game_code):
                if game_code[i] == round_code[i]:
                    black_pegs += 1
                else:
                    game_miss[game_code[i]] += 1
                    round_miss[round_code[i]] += 1

            diff = round_miss - game_miss
            white_pegs = sum(game_miss.values()) - sum(diff.values())

        return [black_pegs, white_pegs]
