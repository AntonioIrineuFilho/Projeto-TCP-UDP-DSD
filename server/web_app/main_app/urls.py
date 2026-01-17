from django.urls import path
from .views import *
from .consumer import *

app_name = "main_app"

urlpatterns = [
    path("", index, name="index")
]

websocket_urlpatterns = [
    path("ws/sensor/", SensorConsumer.as_asgi())
]