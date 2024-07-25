from django.http import HttpResponse
from django.core import serializers
from manager.models import Roster


def index(request):
    data = serializers.serialize('json', Roster.objects.all() )
    return HttpResponse(data, content_type='application/json')

