from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("wallet/", wallet, name="wallet"),
    path("graph/", graph, name="graph"),
    path("conntact/", conntact, name="conntact"),
]
