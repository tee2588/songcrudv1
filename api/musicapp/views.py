from django.shortcuts import render
from rest_framework import generics
from .models import Artiste
from .serializers import ArtisteSerializer

# Create your views here.

class ListArtisteView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


