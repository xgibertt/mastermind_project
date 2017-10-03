from rest_framework import generics, serializers

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

    def perform_create(self, serializer):
        if Game.objects.get(pk=self.kwargs['pk']).ended:
            raise serializers.ValidationError("You cannot play anymore, this game is already ended")

        serializer.save(game_id=self.kwargs['pk'])

    serializer_class = RoundDetailSerializer


class RoundDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows game to be viewed or created.
    """
    queryset = Round.objects.all()
    serializer_class = RoundDetailSerializer
