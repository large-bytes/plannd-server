from django.http import JsonResponse
from models import Roster

# from django.shortcuts import render

# a Python object (dict):
x = {"name": "John", "age": 30, "city": "New York"}


# Create your views here.
def index(request):
    

    return JsonResponse(Roster.objects.all())


# create view to send all data from get all  