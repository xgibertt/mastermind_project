from ..models import Game, Round
from .test_base import BaseTestCase
from rest_framework import status
from django.core.urlresolvers import reverse


class GameTest(BaseTestCase):

    def setUp(self):
        super(GameTest, self).setUp()
        self.url = reverse('game-list')

    def test_should_create_new_game(self):
        self._superuser_login()

        # input
        expected = {"code": self.fake.serialized_code(),
                    "n_rounds": self.fake.n_rounds(),
                    "won": self.fake.boolean()}
        response = self.client.post(self.url, expected, format='json')

        # Check that the response is 201 CREATED.
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Check inserted game properties
        p_id = self._get_id_by_url(response.data.get('url'))
        game = Game.objects.get(pk=p_id)

        self.assertEqual([c[0] for c in expected["code"]], game.code)
        self.assertIsNotNone(game.pk)
        self.assertEqual(expected["n_rounds"], game.n_rounds)
        self.assertEqual(game.won, game.ended)
        self.assertEqual(expected["won"], game.won)

    def test_should_get_game_list(self):
        self._superuser_login()

        # input
        Game.objects.create(code=self.fake.code(),
                            n_rounds=self.fake.n_rounds(),
                            won=self.fake.boolean())

        response = self.client.get(self.url, format='json')

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(1 >= response.data["count"])

    def test_should_get_game_detail(self):
        self._superuser_login()

        # input
        expected = Game.objects.create(code=self.fake.code(),
                                       n_rounds=self.fake.n_rounds(),
                                       won=self.fake.boolean())

        response = self.client.get(reverse('game-detail',
                                           kwargs={'pk': expected.pk}),
                                   format='json')

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Check inserted game properties
        self.assertEqual(expected.pk, response.data["id"])
        self.assertEqual(expected.code, [c[0] for c in response.data["code"]])
        self.assertEqual(expected.n_rounds, response.data["n_rounds"])
        self.assertEqual(expected.ended, response.data["ended"])
        self.assertEqual(expected.won, response.data["won"])


class RoundTest(BaseTestCase):

    def setUp(self):
        super(RoundTest, self).setUp()
        self.game = Game.objects.create(code=self.fake.code(),
                                        n_rounds=self.fake.n_rounds(),
                                        won=self.fake.boolean())
        self.url = reverse('round-list', kwargs={'pk': self.game.pk})

    def test_should_create_new_round(self):
        self._superuser_login()

        # input
        expected = {"code": self.fake.serialized_code(),
                    "black_pegs": self.fake.peg(),
                    "white_pegs": self.fake.peg()}
        response = self.client.post(self.url, expected, format='json')

        # Check that the response is 201 CREATED.
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Check inserted round properties
        p_id = self._get_id_by_url(response.data.get('url'))
        round = Round.objects.get(pk=p_id)

        self.assertIsNotNone(round.pk)
        self.assertEqual([c[0] for c in expected["code"]], round.code)
        self.assertEqual(expected["black_pegs"], round.black_pegs)
        self.assertEqual(expected["white_pegs"], round.white_pegs)
        self.assertEqual(self.game, round.game)

    def test_should_get_round_list(self):
        self._superuser_login()

        # input
        Round.objects.create(code=self.fake.code(),
                             black_pegs=self.fake.peg(),
                             white_pegs=self.fake.peg(),
                             game=self.game)

        response = self.client.get(self.url, format='json')

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(1 >= response.data["count"])

    def test_should_get_round_detail(self):
        self._superuser_login()

        # input
        expected = Round.objects.create(code=self.fake.code(),
                                        black_pegs=self.fake.peg(),
                                        white_pegs=self.fake.peg(),
                                        game=self.game)

        response = self.client.get(reverse('round-detail',
                                           kwargs={'pk': expected.pk}),
                                   format='json')

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Check inserted round properties
        self.assertEqual(expected.code, [c[0] for c in response.data["code"]])
        self.assertEqual(expected.black_pegs, response.data["black_pegs"])
        self.assertEqual(expected.white_pegs, response.data["white_pegs"])
        self.assertEqual(self.game.pk, self._get_id_by_url(response.data.get('game')))
