from rest_framework import serializers
from .models import Roster


class RosterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roster
        fields = "__all__"
