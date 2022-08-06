from django.db import models

class AudioFile(models.Model):
    path = models.CharField(max_length=2048, primary_key=True)
    filename = models.CharField(max_length=1024)

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    value = models.CharField(max_length=255)
    
class Musician(models.Model):
    name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)

class Alias(models.Model):
    name = models.ForeignKey(to=Musician, related_name='alias_name', on_delete=models.CASCADE)
    alias = models.ForeignKey(to=Musician, on_delete=models.CASCADE)

class Album(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    musicians = models.ManyToManyField(to=Musician)

class Music(models.Model):
    name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    audiofile = models.ForeignKey(to=AudioFile, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
    musicians = models.ManyToManyField(to=Musician)
    tags = models.ManyToManyField(to=Tag)

class User(models.Model):
    name = models.CharField(max_length=255)

class Rating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    music = models.ForeignKey(to=Music, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
