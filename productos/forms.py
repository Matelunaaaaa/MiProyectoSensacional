from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['correo_electronico', 'nombre', 'apellido_paterno', 'apellido_materno', 'contraseña', 'genero']