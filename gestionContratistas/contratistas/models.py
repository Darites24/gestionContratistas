from django.db import models
from django.contrib.auth.models import User

class Contratista(models.Model):
    nombre = models.CharField(max_length=100)
    perfil = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)


class Contrato(models.Model):
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    estado = models.CharField(max_length=10, choices=[('activo','Activo'), ('inactivo','Inactivo')])

class RegistroAccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

