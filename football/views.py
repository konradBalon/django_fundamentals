from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_page(request):
    return HttpResponse("Hello World form Football app")
