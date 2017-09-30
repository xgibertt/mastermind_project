from rest_framework import generics

from .models import Game, Round
from .serializers import GameListSerializer, GameDetailSerializer, RoundDetailSerializer


class GameList(generics.ListCreateAPIView):
    """
    API endpoint that allows game to be viewed or created.
    """
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows game to be viewed or created.
    """
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer


class RoundList(generics.ListCreateAPIView):
    """
    API endpoint that allows game to be viewed or created.
    """
    def get_queryset(self):
        game_pk = self.kwargs['pk']
        return Round.objects.filter(game__pk=game_pk)

    serializer_class = RoundDetailSerializer


class RoundDetail(generics.ListCreateAPIView):
    """
    API endpoint that allows game to be viewed or created.
    """
    queryset = Round.objects.all()
    serializer_class = RoundDetailSerializer