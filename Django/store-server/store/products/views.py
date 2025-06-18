from importlib.resources import contents

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'Test Title',
               'username':'valeri',
               }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products' : [
                    {'image' : '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                       'name' : 'Синяя куртка The North Face',
                       'price' : 23725,
                       'description' : 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                       },
        ]
    }
    return render(request, 'products/products.html', context)