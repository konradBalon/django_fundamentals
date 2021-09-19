from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directors')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='screenplays')
    starring = models.ManyToManyField(
        Person,
        through='PersonMovie',
        through_fields=('movie', 'person'))
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre)


genre = ''


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)


#

#     # insert dummy data to DB


# p1 = Person.objects.create(first_name='Ada', last_name='Zjada')
# p2 = Person.objects.create(first_name='Michal', last_name='Kichal')
# p3 = Person.objects.create(first_name='Grazyna', last_name='Wyzyna')
# p4 = Person.objects.create(first_name='Michal', last_name='Popychal')
# #
# m1 = Movie.objects.create(title='The lord of the board', director=p1, screenplay=p1, year=2002, rating=2)
# m2 = Movie.objects.create(title='The lord of destruction', director=p4, screenplay=p1, year=1992, rating=6)
#
#
# # m1.starring.set(((p1, 'figurant'), p2, p3, p4))
