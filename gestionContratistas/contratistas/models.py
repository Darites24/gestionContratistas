from django.db import models
from django.contrib.auth.models import User

class Profesion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class NivelEducativo(models.Model):
    nombre = models.CharField(max_length=100)
    honorarios = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Contratista(models.Model):
    nombre = models.CharField(max_length=100)
    perfil = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE, null=True, blank=True)
    nivel_educativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE, null=True, blank=True)


class Contrato(models.Model):
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    estado = models.CharField(max_length=10, choices=[('activo','Activo'), ('inactivo','Inactivo')])
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class RegistroAccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

