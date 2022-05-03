from django.urls import path
from .views import *
from .dash.apps import historical_data

urlpatterns = [
    path("", home, name="home"),
    path("wallet/", wallet, name="wallet"),
    path("graph/", graph, name="graph"),
    path("contact/", contact, name="contact"),
]
