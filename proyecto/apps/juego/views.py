"""from django import http"""
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html',texto)



def contact(request):
    return HttpResponse("Hola estoy en la pagina de contacto")