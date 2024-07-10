from django.http import HttpResponse

# from django.shortcuts import render
import json

# a Python object (dict):
x = {"name": "John", "age": 30, "city": "New York"}


# Create your views here.
def index(request):
    return HttpResponse(json.dumps(x))
