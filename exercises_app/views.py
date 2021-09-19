from django.http import HttpResponse

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


def hello(request):
    return HttpResponse('hello from Exercise_app!')
