from django.http import HttpResponse

from django.shortcuts import render
from . import models

def inicio(request):
    return HttpResponse("Hola mundo desde django")

def lista_productos(request):
    productos = models.Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})