from django.urls import re_path
from .consumers import ChatConsumer

# URL used for websockets
websocket_urlpatterns = [
	re_path(r'ws/zoso/chat/(?P<roomname>\w+)/$', ChatConsumer.as_asgi())
]