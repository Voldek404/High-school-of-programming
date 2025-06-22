from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request, cat):
    if (request.GET):
        print(request.GET)

    return HttpResponse("<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=False)  # 302
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')