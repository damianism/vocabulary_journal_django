from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def home_view(request):
    return render(request, "home/home.html")


def about_view(request):
    """ view to render the about template """
    return render(request, "home/about.html")
