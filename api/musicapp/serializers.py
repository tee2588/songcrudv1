from rest_framework import serializers
from .models import Artiste


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ("first_name", "last_name", "age")