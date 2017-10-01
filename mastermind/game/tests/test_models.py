from ..models import Game, Round
from .test_base import BaseTestCase


class GameTest(BaseTestCase):
    def setUp(self):
        super(GameTest, self).setUp()

        # random inputs
        self.expected_code = self.fake.code()
        self.expected_ended = self.fake.boolean()
        self.expected_won = self.fake.boolean()

    def test_should_create_new_game(self):
        game = Game.objects.create(
            code=self.expected_code,
            ended=self.expected_ended,
            won=self.expected_won,
        )

        self.assertIsNotNone(game.pk)
        self.assertEqual(self.expected_code, game.code)
        self.assertEqual(self.expected_ended, game.ended)
        self.assertEqual(self.expected_won, game.won)

    def test_should_retrieve_game(self):
        expected = Game.objects.create(
            code=self.expected_code,
            ended=self.expected_ended,
            won=self.expected_won,
        )

        game = Game.objects.get(pk=expected.pk)

        self.assertEqual(expected.pk, game.pk)
        self.assertEqual(expected.code, game.code)
        self.assertEqual(expected.ended, game.ended)
        self.assertEqual(expected.won, game.won)

    def test_should_update_game(self):
        expected = Game.objects.create(
            code=self.expected_code,
            ended=self.expected_ended,
            won=self.expected_won,
        )

        new_code = self.fake.code()
        expected.code = new_code
        expected.save()

        game = Game.objects.get(pk=expected.pk)

        self.assertEqual(expected.pk, game.pk)
        self.assertEqual(new_code, game.code)
        self.assertEqual(expected.ended, game.ended)
        self.assertEqual(expected.won, game.won)


class RoundTest(BaseTestCase):
    def setUp(self):
        super(RoundTest, self).setUp()

        # random inputs
        self.expected_code = self.fake.code()
        self.expected_black_pegs = self.fake.peg()
        self.expected_white_pegs = self.fake.peg()
        self.game = Game.objects.create(
            code=self.expected_code,
            ended=False,
            won=False,
        )

    def test_should_create_new_round(self):
        round = Round.objects.create(
            code=self.expected_code,
            black_pegs=self.expected_black_pegs,
            white_pegs=self.expected_white_pegs,
            game=self.game
        )

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertEqual(self.expected_black_pegs, round.black_pegs)
        self.assertEqual(self.expected_white_pegs, round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_retrieve_round(self):
        expected = Round.objects.create(
            code=self.expected_code,
            black_pegs=self.expected_black_pegs,
            white_pegs=self.expected_white_pegs,
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertEqual(self.expected_black_pegs, round.black_pegs)
        self.assertEqual(self.expected_white_pegs, round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_retrieve_rounds_by_game(self):
        expected = Round.objects.create(
            code=self.expected_code,
            black_pegs=self.expected_black_pegs,
            white_pegs=self.expected_white_pegs,
            game=self.game
        )

        round = Round.objects.get(game__pk=expected.game.pk)

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertEqual(self.expected_black_pegs, round.black_pegs)
        self.assertEqual(self.expected_white_pegs, round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_update_round(self):
        expected = Round.objects.create(
            code=self.expected_code,
            black_pegs=self.expected_black_pegs,
            white_pegs=self.expected_white_pegs,
            game=self.game
        )

        new_code = self.fake.code()
        expected.code = new_code
        expected.save()

        round = Round.objects.get(pk=expected.pk)

        self.assertEqual(new_code, round.code)
        self.assertEqual(self.expected_black_pegs, round.black_pegs)
        self.assertEqual(self.expected_white_pegs, round.white_pegs)
        self.assertEqual(self.game, round.game)
