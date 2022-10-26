import imp
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

class Song(models.Model):
    
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.IntegerField()
    artist_id = models.IntegerField()

class Lyric(models.Model):
    jam = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    song_id = models.IntegerField()



