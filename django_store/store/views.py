from django.shortcuts import render
from django.http import HttpResponse
import random

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

    context = {'lucky_number': lucky_number,
               'user_number': user_number,
               'user_name': user,
               'fruits': fruits,
               'guest_list': guest_list}

    return render(request, 'my_page.html', context)


def hello_me(request):
    name = 'Alexander'
    return HttpResponse('Hello. My name is ' + name)