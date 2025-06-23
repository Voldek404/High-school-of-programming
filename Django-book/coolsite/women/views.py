from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})

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