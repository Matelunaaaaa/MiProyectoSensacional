from django.db import models

# Create your models here.

class cliente(models.Model):
    correo = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=40) 
    aparterno = models.CharField(max_length=40)
    amaterno = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')


    def __str__(self):
        return str(self.nombre)+" "+str(self.aparterno)
    
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)