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
    def scatter():
        x1 = [1, 2, 3, 4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y=y1,
        )
        layout = dict(
            title="Simple Graph",
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)]),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type="div", include_plotlyjs=False)
        return plot_div

    context = {"plot1": scatter()}

    return render(request, "graph.html", context)


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
