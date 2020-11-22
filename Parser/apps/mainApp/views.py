from django.shortcuts import render
from .PythonScripts import habrParser


def index(request):
    a = habrParser.habr_themes()
    data = {"links" : a}

    return render(request, 'windows/main.html', context = data)
