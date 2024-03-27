from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("HOMEPAGE")
    return render(request, "homepage.html")


def about(request):
    # return HttpResponse("ABOUT")
    return render(request, "about.html")
