from rest_framework import generics

from .models import Game, Round
from .serializers import GameListSerializer, GameDetailSerializer


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
