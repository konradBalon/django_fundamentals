from django.http import HttpResponse
from django.shortcuts import render
from homework_app.models import Movie, Person, PersonMovie
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, MovieForm


# Create your views here.
def hello_page(request):
    return HttpResponse("Hello World form homework app")


def get_movie(request, movie_id):
    m = Movie.objects.filter(id=movie_id)
    response = "<p><strong> id  &emsp; title &emsp;    year&emsp;    director &emsp;  rating</p> </strong><br>"
    response += f'{m[0].id}  &emsp; {m[0].title} &emsp; {m[0].director.first_name} {m[0].director.last_name} &emsp; {m[0].rating} '
    return HttpResponse(response)


def get_persons(request):
    link = '<a href="/homework/edit-person/{}">Edit</a>'
    body = [f'{(p.first_name, p.last_name, p.id), link.format(p.id)},   <br>' for p in Person.objects.all()].__str__()
    button = """<a href='/homework/add-person'">
            <button>Add Person</button>
            </a>
            """
    return HttpResponse(body + '<br>' + button)


def edit_person(request, id):
    p = Person.objects.filter(id=id)[0]
    print(p.__dict__)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            Person.objects.filter(id=id).update(first_name=first_name, last_name=last_name)
            return HttpResponseRedirect('/homework/persons')
    else:
        form = NameForm(initial={'first_name': p.first_name, 'last_name': p.last_name})
    return render(request, 'name.html', {'form': form})


def add_person(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('get request occurs')
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = NameForm(request.POST)
        print(form['first_name'].value())
        print(form['last_name'].value())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            print((first_name, last_name))
            # redirect to a new URL:
            Person.objects.create(first_name=first_name, last_name=last_name)
            return HttpResponseRedirect('/homework/persons')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def get_movies(request):
    link = '<a href="/homework/edit-movie/{}">Edit</a>'
    body = [f'{(m.title, m.year, m.director.first_name, m.director.last_name), link.format(m.id)},   <br>' for m in
            Movie.objects.all().order_by('year')].__str__()
    button = """<a href='/homework/add-movie'">
            <button>Add Movie</button>
            </a>
            """
    return HttpResponse(body + '<br>' + button)


def edit_movie(request, id):
    m = Movie.objects.filter(id=id)[0]
    print(m.__dict__)
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            director_f = form.cleaned_data['director'].split()[0]
            director_l = form.cleaned_data['director'].split()[1]
            d = Person.objects.create(first_name=director_f, last_name=director_l)
            Movie.objects.filter(id=id).update(title=title, year=year, director=d)
            return HttpResponseRedirect('/homework/movies')
    else:
        form = MovieForm(
            initial={'title': m.title, 'year': m.year, 'director': f'{m.director.first_name} {m.director.last_name}'})
    return render(request, 'name.html', {'form': form})


def add_movie(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            rating = form.cleaned_data['rating']

            director_f = form.cleaned_data['director'].split()[0]
            director_l = form.cleaned_data['director'].split()[1]
            screenplay_f = form.cleaned_data['screenplay'].split()[0]
            screenplay_l = form.cleaned_data['screenplay'].split()[1]
            d = Person.objects.create(first_name=director_f, last_name=director_l)
            s = Person.objects.create(first_name=screenplay_f, last_name=screenplay_l)
            Movie.objects.create(title=title, year=year, director=d, rating=rating, screenplay=s)
            return HttpResponseRedirect('/homework/movies')
    else:
        form = MovieForm()

    return render(request, 'name.html', {'form': form})
