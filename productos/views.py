from django.shortcuts import render , get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuarios
from .forms import UsuariosForm
from django.contrib.auth import authenticate, login

# Create your views here.

def Principal(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'Principal.html', {'usuario': usuario})



def InicioSesion(request,pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'InicioSesion.html', {'usuario': usuario})

def ayuda(request):
    context={}
    return render(request, 'ayuda.html', context)

def catalogo(request):
    context={}
    return render(request, 'catalogo.html', context)

def razas(request):
    context={}
    return render(request, 'razas.html', context)


def usuario_list(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

@csrf_exempt
def registrarse(request):
    context={}
    return render(request, 'registrarse.html', context)

def usuario_create(request):
    if request.method == 'POST':
        correo_electronico = request.POST.get('correo_electronico')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        contraseña = request.POST.get('contraseña')
        genero = request.POST.get('genero')

        usuario = Usuarios(
            correo_electronico=correo_electronico,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            contraseña=contraseña,
            genero=genero
        )
        usuario.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
    

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})