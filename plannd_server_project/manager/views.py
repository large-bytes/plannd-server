from django.http import HttpResponse
from django.core import serializers
from manager.models import Roster
from .serializers import RosterSerializer
from rest_framework import viewsets


# def index(request):
#     data = serializers.serialize('json', Roster.objects.all() )
#     return HttpResponse(data, content_type='application/json')


class RosterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
