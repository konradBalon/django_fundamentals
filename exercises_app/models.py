import random

from django.db import models


# Create your models here.
class Band(models.Model):
    GENRE_CHOICES = (
        (-1, 'not defined'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (2, 'pop'),

        (3, 'hip - hop,'),
        (4, 'electronic'),
        (5, 'reggae'),
        (6, 'other')
    )

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=-1)

    def print(self):
        return f'{self.name},{self.year},{self.still_active},{self.genre}'

    @staticmethod
    def fill_empty_years():
        all_bands = Band.objects.filter(year=None)
        print([(band.name, band.id) for band in all_bands])
        for band in all_bands:
            band.year = random.randint(2030, 2050)
            band.save()

    @staticmethod
    def fill_empty_prop():

        all_bands = Band.objects.filter(still_active=True)
        print([band.__dict__ for band in all_bands])
        for band in all_bands:
            band.genre = random.randint(0, 6)
            band.still_active = random.choice([True, False])
            band.save()


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()


class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'writing in progress'),
        (2, 'waiting for approval'),
        (3, 'published'))
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    date_publish = models.DateTimeField(null=True)
    date_unpublish = models.DateTimeField(null=True)


class Album(models.Model):
    CHOICES = (
        (0, ''),
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
        (6, '******'),
    )
    title = models.CharField(max_length=64)
    released_year = models.IntegerField()
    score = models.IntegerField(choices=CHOICES)
