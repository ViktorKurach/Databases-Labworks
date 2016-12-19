from django.db import models


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    style = models.CharField(max_length=40)

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    genre_id = models.ForeignKey(Genre)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    since = models.IntegerField()

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey(Artist)
    label_id = models.ForeignKey(Label)
    year = models.IntegerField()
    tracks = models.IntegerField()
    duration = models.TimeField()
