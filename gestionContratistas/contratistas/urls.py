from django.urls import path
from .views import listarContratistas, crearContratista, editarContratista, eliminarContratista, detalleContratista
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', listarContratistas, name='listarContratistas'),
    path('crear/', crearContratista, name='crearContratista'),
    path('editar/<int:pk>/', editarContratista, name='editarContratista'),
    path('eliminar/<int:pk>/', eliminarContratista, name='eliminarContratista'),
    path('detalle/<int:pk>/', detalleContratista, name='detalleContratista'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)