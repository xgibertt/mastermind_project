from rest_framework import serializers

from .models import Game, Round


class GameListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="game-detail",)
    round_count = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = ('url', 'id', 'code', 'round_count', 'ended', 'won',)


class GameDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="game-detail",)
    rounds = serializers.HyperlinkedRelatedField(many=True,
                                                 read_only=True,
                                                 view_name="round-detail")

    class Meta:
        model = Game
        fields = ('url', 'id', 'code', 'rounds', 'ended', 'won', 'rounds',)


class RoundDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="round-detail", )
    game = serializers.HyperlinkedRelatedField(read_only=True, view_name="game-detail", )

    class Meta:
        model = Round
        fields = ('url', 'id', 'game', 'code', 'black_pegs', 'white_pegs',)
