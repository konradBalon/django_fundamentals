from django.conf.urls import url
from django.http import HttpResponse
from django.urls import path
from football import views
urlpatterns = [
    path('', views.hello_page),

]

