from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def wallet(request):
    return render(
        request,
        "wallet.html",
    )


def graph(request):
    return render(request, "graph.html")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
