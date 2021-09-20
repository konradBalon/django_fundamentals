from django.conf.urls import url
from django.http import HttpResponse
from django.urls import path
from homework_app import views
urlpatterns = [
    path('', views.hello_page),
    path('movies', views.get_movies),
    path('edit-movie/<int:id>', views.edit_movie),
    path('add-movie/', views.add_movie),
    path('movie-details/<int:movie_id>', views.get_movie),
    path('persons', views.get_persons),
    path('edit-person/<int:id>', views.edit_person),
    path('add-person', views.add_person),

]

