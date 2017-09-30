from rest_framework import serializers

from .models import Game


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
