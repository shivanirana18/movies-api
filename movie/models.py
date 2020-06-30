from django.db import models

# Create your models here.

class Genre(models.Model):
    '''
    Genre model
    '''
    name = models.CharField(max_length=100, blank=False, db_column='name')

    class Meta:
        ''' Meta class to set table name'''
        db_table = 'genre'

class Movie(models.Model):
    '''
    movie table
    '''
    primaryid = models.AutoField(primary_key=True, db_column='primaryid')
    director = models.CharField(max_length=32, blank=False, db_column='director')
    popularity = models.FloatField(blank=True, null=True, db_column='99popularity')
    imdbscore = models.FloatField(blank=True, null=True, db_column='imdb_score')
    name = models.CharField(max_length=32, blank=False, db_column='name')
    genre = models.ManyToManyField(Genre)

    class Meta:
        ''' Meta class to set table name'''
        db_table = 'movies'
