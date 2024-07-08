from django.shortcuts import render
from .models import cliente, Genero
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@login_required
def Principal(request):
    context={}
    return render(request, 'Principal.html', context)

def InicioSesion(request):
    context={}
    return render(request, 'InicioSesion.html', context)
@login_required
def ayuda(request):
    context={}
    return render(request, 'ayuda.html', context)
@login_required
def catalogo(request):
    context={}
    return render(request, 'catalogo.html', context)
@login_required
def razas(request):
    context={}
    return render(request, 'razas.html', context)

def registrarse(request):
    if request.method != "POST":
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
        obj = cliente.objects.create( correo = correo,
                                      nombre = nombre,
                                      aparterno = apaterno,
                                      amaterno = amaterno,
                                      contraseña = contraseña,
                                      id_genero = obGenero )
        obj.save()
        context={'mensaje':'registrado con exito'}
        return render(request, 'registrarse.html', context)
    

def menu(request):
    request.session["usuario"]="scabrera"
    usuario=request.session["usuario"]
    context ={'usuario':usuario}
    return render(request, 'Principal.html', context)

@staff_member_required
def admin(request):
    admin = cliente.objects.all()
    context={'admin': admin}
    return render(request, 'admin.html', context)

@staff_member_required
def borrar_cliente(request, pk):
    context={}
    try:
        borrar = cliente.objects.get(correo=pk)

        borrar.delete()
        mensaje="se ha borrado con exito"
        borrar = cliente.objects.all()
        context = {'borrar': borrar, 'mensaje':mensaje}
        return render(request, 'admin.html', context)
    except:
        mensaje = "Error"
        borrar = cliente.objects.all()
        context = {'borrar': borrar, 'mensaje':mensaje}
        return render(request, 'admin.html', context)

def editar_cliente(request, pk):
    if pk != "":
        editar=cliente.objects.get(correo=pk)
        generos=Genero.objects.all()

        print(type(editar.id_genero.genero))

        context={'editar':editar, 'generos':generos}
        if editar:
            return render(request, 'editar_clientes.html', context)
        else:
            context={'mensaje':"error al editar"}
            return render(request, 'admin.html', context)
        
def editarClientes(request):
    if request.method=='POST':
        correo=request.POST["correo"]
        nombre=request.POST["nombre"]
        aparterno=request.POST["aparterno"]
        amaterno=request.POST["amaterno"]
        contraseña=request.POST["contraseña"]
        genero = request.POST["genero"]

        objGenero = Genero.objects.get(id_genero = genero)
        
        editar = cliente()
        editar.correo=correo
        editar.nombre=nombre
        editar.aparterno=aparterno
        editar.amaterno=amaterno
        editar.contraseña=contraseña
        editar.id_genero=objGenero
        editar.save()

        generos =Genero.objects.all()
        context={'mensaje':"datos editados", 'generos':generos, 'editar':editar}
        return render(request, 'admin.html', context)

    else:
        clientesEdita = cliente.objects.all()
        context={'editar':clientesEdita}
        return render(request, 'admin.html', context)