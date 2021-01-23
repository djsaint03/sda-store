from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Product

# Create your views here.

guest_list = {
    'sony': 'beer',
    'alexander': 'doritos',
    'elina': 'beer',
    'robert': 'cake'
}

secret_password = 'snow'

def hello(request, user):
    lucky_number = random.randint(1, 100)
    user_number = request.GET.get('mynumber')

    fruits = ['orange', 'banada', 'apple']

    promotion = True


    context = {'lucky_number': lucky_number,
               'user_number': user_number,
               'user_name': user,
               'fruits': fruits,
               'guest_list': guest_list,
               'promotion': promotion,
               }

    return render(request, 'my_page.html', context)


def hello_me(request):
    name = 'Alexander'
    return HttpResponse('Hello. My name is ' + name)


def products_list(request):

    products = Product.objects.all()
    total_products = products.count()

    promotion = True

    context = {
        'products': products,
        'promotion': promotion,
        'total_products': total_products
    }

    return render(request, 'products_list.html', context)