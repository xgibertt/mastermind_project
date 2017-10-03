from rest_framework import serializers

from .models import Game, Round, COLORS, COLORS_VALUES


class CodeField(serializers.Field):
    """
    Color objects
    """
    def to_representation(self, obj):
        return [c for c in map(lambda c: dict(COLORS)[c], obj)]

    def to_internal_value(self, data):
        return [c for c in map(lambda c: COLORS_VALUES[c], data)]


class GameListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="game-detail",)
    code = CodeField()
    ended = serializers.ReadOnlyField()
    round_count = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = ('url', 'id', 'code', 'n_rounds', 'ended', 'won', 'round_count')


class GameDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="game-detail",)
    code = CodeField()
    ended = serializers.ReadOnlyField()
    rounds = serializers.HyperlinkedRelatedField(many=True,
                                                 read_only=True,
                                                 view_name="round-detail")

    class Meta:
        model = Game
        fields = ('url', 'id', 'code', 'n_rounds', 'ended', 'won', 'rounds',)


class RoundDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="round-detail", )
    game = serializers.HyperlinkedRelatedField(read_only=True, view_name="game-detail", )
    code = CodeField()
    black_pegs = serializers.ReadOnlyField()
    white_pegs = serializers.ReadOnlyField()

    class Meta:
        model = Round
        fields = ('url', 'id', 'game', 'code', 'black_pegs', 'white_pegs',)
