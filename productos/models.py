from django.db import models

# Create your models here.

class Usuarios(models.Model):

    correo_electronico = models.EmailField(max_length=254, unique=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128)
    genero = models.CharField(max_length=1)

    def str(self):
        return self.nombre