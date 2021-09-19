from django.http import HttpResponse
from django.shortcuts import render
from homework_app.models import Movie, Person, PersonMovie


# Create your views here.
def hello_page(request):
    return HttpResponse("Hello World form homework app")


def get_movies(request):
    movies = "<p><strong> title &emsp; year&emsp;    director&emsp;    rating </p> </strong><br>"
    movies += [
        f'ID:{m.id}&emsp;{m.title} &emsp; {m.year}&emsp;{m.director.first_name} {m.director.last_name}&emsp; {m.rating}<br>'
        for
        m in Movie.objects.order_by('year')].__str__()

    return HttpResponse(movies.replace('[', '').replace(']', '').replace(',', '').replace('\'', ''))


def get_movie(request, movie_id):
    m = Movie.objects.filter(id=movie_id)
    response =  "<p><strong> id  &emsp; title &emsp;    year&emsp;    director &emsp;  rating</p> </strong><br>"
    response += f'{m[0].id}  &emsp; {m[0].title} &emsp; {m[0].director.first_name} {m[0].director.last_name} &emsp; {m[0].rating} '
    return HttpResponse(response)
