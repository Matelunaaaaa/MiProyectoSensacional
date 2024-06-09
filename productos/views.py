from django.shortcuts import render

# Create your views here.

def Principal(request):
    context={}
    return render(request, 'Principal.html', context)

def InicioSesion(request):
    context={}
    return render(request, 'InicioSesion.html', context)

def ayuda(request):
    context={}
    return render(request, 'ayuda.html', context)

def catalogo(request):
    context={}
    return render(request, 'catalogo.html', context)
