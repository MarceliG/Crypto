from django.shortcuts import render


def wallet(request):
    return render(
        request,
        "wallet.html",
    )


def graph(request):
    return render(
        request,
        "graph.html",
    )


def home(request):
    return render(
        request,
        "home.html",
    )
