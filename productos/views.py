from django.shortcuts import render , get_object_or_404, redirect
from .models import Usuarios
from .forms import UsuariosForm

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

def registrarse(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal/0/')
    else:
        form = UsuariosForm()
    return render(request, 'Principal.html', {'form': form})

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