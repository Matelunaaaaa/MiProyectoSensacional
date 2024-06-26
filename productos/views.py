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

def ayuda(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'ayuda.html', {'usuario': usuario})

def catalogo(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'catalogo.html', {'usuario': usuario})

def razas(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'razas.html', {'usuario': usuario})


def usuario_list(request, pk):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

@csrf_exempt
def registrarse(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    return render(request, 'registrarse.html', {'usuario': usuario})

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

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        correo_electronico1 = request.POST.get('correo_electronico')
        password = request.POST.get('password')

        try:
            usuario = Usuarios.objects.get(correo_electronico=correo_electronico1)
        except Usuarios.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'El correo electrónico no está registrado.'})

        if usuario:
            if usuario.contraseña == password:
                # Autenticación manual (no usando authenticate de Django)
                #login(request, usuario)
                return JsonResponse({'success': True, 'usuario': usuario.id})
            else:
                return JsonResponse({'success': False, 'error': 'Contraseña incorrecta.'})

    return JsonResponse({'success': False, 'error': 'Método de solicitud inválido.'})