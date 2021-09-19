from django.conf.urls import url
from django.http import HttpResponse
from django.urls import path
from exercises_app import views
urlpatterns = [
    path('', views.hello),
    path('articles', views.get_articles),

]

