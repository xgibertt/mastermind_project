from django.conf.urls import url, include
from .views import GameList, GameDetail


urlpatterns = [
    url(r'^game/$', GameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>\d+)/$', GameDetail.as_view(), name='game-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]