from ..models import Game, Round
from .test_base import BaseTestCase


class GameTest(BaseTestCase):
    def setUp(self):
        super(GameTest, self).setUp()

        # random inputs
        self.expected_code = self.fake.code()
        self.expected_n_rounds = self.fake.n_rounds()
        self.expected_won = self.fake.boolean()

    def test_should_create_new_game(self):
        game = Game.objects.create(
            code=self.expected_code,
            n_rounds=self.expected_n_rounds,
            won=self.expected_won,
        )

        self.assertIsNotNone(game.pk)
        self.assertEqual(self.expected_code, game.code)
        self.assertEqual(self.expected_n_rounds, game.n_rounds)
        self.assertEqual(self.expected_won, game.won)
        self.assertEqual(0, game.round_count)
        self.assertEqual(self.expected_won, game.ended)

    def test_should_retrieve_game(self):
        expected = Game.objects.create(
            code=self.expected_code,
            n_rounds=self.expected_n_rounds,
            won=self.expected_won,
        )

        game = Game.objects.get(pk=expected.pk)

        self.assertEqual(expected.pk, game.pk)
        self.assertEqual(expected.code, game.code)
        self.assertEqual(expected.n_rounds, game.n_rounds)
        self.assertEqual(expected.won, game.won)
        self.assertEqual(0, game.round_count)
        self.assertEqual(game.won, game.ended)

    def test_should_update_game(self):
        expected = Game.objects.create(
            code=self.expected_code,
            n_rounds=self.expected_n_rounds,
            won=self.expected_won,
        )

        new_code = self.fake.code()
        expected.code = new_code
        expected.save()

        game = Game.objects.get(pk=expected.pk)

        self.assertEqual(expected.pk, game.pk)
        self.assertEqual(expected.code, game.code)
        self.assertEqual(expected.n_rounds, game.n_rounds)
        self.assertEqual(expected.won, game.won)
        self.assertEqual(0, game.round_count)
        self.assertEqual(game.won, game.ended)


class RoundTest(BaseTestCase):
    def setUp(self):
        super(RoundTest, self).setUp()

        # random inputs
        self.expected_code = self.fake.code()
        self.game = Game.objects.create(
            code=self.fake.code(),
            n_rounds=self.fake.n_rounds(),
            won=self.fake.boolean(),
        )

    def test_should_create_new_round(self):
        round = Round.objects.create(
            code=self.expected_code,
            game=self.game
        )

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertIsNotNone(round.black_pegs)
        self.assertIsNotNone(round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_retrieve_round(self):
        expected = Round.objects.create(
            code=self.expected_code,
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertIsNotNone(round.black_pegs)
        self.assertIsNotNone(round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_retrieve_rounds_by_game(self):
        expected = Round.objects.create(
            code=self.expected_code,
            game=self.game
        )

        round = Round.objects.get(game__pk=expected.game.pk)

        self.assertIsNotNone(round.pk)
        self.assertEqual(self.expected_code, round.code)
        self.assertEqual(self.game, round.game)

    def test_should_update_round(self):
        expected = Round.objects.create(
            code=self.expected_code,
            game=self.game
        )

        new_code = self.fake.code()
        expected.code = new_code
        expected.save()

        round = Round.objects.get(pk=expected.pk)

        self.assertEqual(new_code, round.code)
        self.assertIsNotNone(round.black_pegs)
        self.assertIsNotNone(round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_mark_game_as_won_when_both_codes_are_the_same(self):
        self.game = Game.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            n_rounds=self.fake.n_rounds(),
        )

        expected = Round.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertTrue(round.game.won)

    def test_should_game_won_be_false_when_both_codes_are_distinct(self):
        self.game = Game.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            n_rounds=self.fake.n_rounds(),
        )

        expected = Round.objects.create(
            code=['R', 'R', 'R', 'R'],
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertFalse(round.game.won)

    def test_should_get_4_black_and_0_white_pegs_when_code_are_the_same(self):
        self.game = Game.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            n_rounds=self.fake.n_rounds(),
        )

        expected = Round.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertEqual(4, round.black_pegs)
        self.assertEqual(0, round.white_pegs)

    def test_should_get_0_black_and_0_white_pegs_when_all_colors_are_distinct(self):
        self.game = Game.objects.create(
            code=['Y', 'Y', 'Y', 'Y'],
            n_rounds=self.fake.n_rounds(),
        )

        expected = Round.objects.create(
            code=['R', 'R', 'R', 'R'],
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertEqual(0, round.black_pegs)
        self.assertEqual(0, round.white_pegs)

    def test_should_get_2_black_and_2_white_pegs_when_2_colors_are_equal_and_2_colors_in_different_positions(self):
        self.game = Game.objects.create(
            code=['B', 'R', 'Y', 'G'],
            n_rounds=self.fake.n_rounds(),
        )

        expected = Round.objects.create(
            code=['Y', 'R', 'B', 'G'],
            game=self.game
        )

        round = Round.objects.get(pk=expected.pk)

        self.assertEqual(2, round.black_pegs)
        self.assertEqual(2, round.white_pegs)
