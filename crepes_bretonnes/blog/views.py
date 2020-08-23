from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse('<h1>Welcome Dude</h1>')


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def somme(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/somme.html', locals())
