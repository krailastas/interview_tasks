from django.urls import re_path

from . import notifications


websocket_urlpatterns = [
    re_path(r'ws/notification/$', notifications.Notifications),
]