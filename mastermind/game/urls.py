from django.conf.urls import url, include
from .views import GameList, GameDetail, RoundList, RoundDetail


urlpatterns = [
    url(r'^games/$', GameList.as_view(), name='game-list'),
    url(r'^games/(?P<pk>\d+)/$', GameDetail.as_view(), name='game-detail'),
    url(r'^games/(?P<pk>\d+)/rounds$', RoundList.as_view(), name='round-list'),
    url(r'^rounds/(?P<pk>\d+)/$', RoundDetail.as_view(), name='round-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]