from django.shortcuts import render
from functions.script import scrap

def home(request):

    z = scrap()
    return render(request, 'home.html', {'sum':z})