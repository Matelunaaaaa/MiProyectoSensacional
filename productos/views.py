from django.shortcuts import render
from .models import cliente, Genero

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

def razas(request):
    context={}
    return render(request, 'razas.html', context)

def registro(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'registrarse.html', context)
    
    else:
        correo = request.POST['correo']
        nombre = request.POST['nombre']
        apaterno = request.POST['apaterno']
        amaterno = request.POST['amaterno']
        contraseña = request.POST['contraseña']
        genero = request.POST['genero']

        obGenero =Genero.objects.get(id_genero = genero)
        obj = cliente.objects.create( correo = correo ,
                                      nombre = nombre,
                                      apaterno = apaterno,
                                      amaterno = amaterno,
                                      contraseña = contraseña,
                                      id_genero = obGenero )
        obj.save()
        context={'mensaje':'registrado con exito'}
        return render(request, 'registrarse.html', context)