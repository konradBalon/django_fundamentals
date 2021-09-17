from django.conf.urls import url
from django.http import HttpResponse
from django.urls import path
from homework_app import views
urlpatterns = [
    path('', views.hello_page),
]

