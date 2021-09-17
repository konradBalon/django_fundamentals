from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from exercises_app.models import Article


def get_articles(request):
    results = []
    for a in Article.objects.filter(status=1):
        results.append({
            'title': a.title,
            'author': a.author,
            'date_added': a.date_publish,
        })
    return HttpResponse(str(results))
