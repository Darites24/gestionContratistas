from django.urls import path
from .views import listarContratistas, crearContratista, editarContratista, eliminarContratista, detalleContratista, crearContrato
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('listar/', listarContratistas, name='listarContratistas'),
    path('crear/', crearContratista, name='crearContratista'),
    path('editar/<int:pk>/', editarContratista, name='editarContratista'),
    path('eliminar/<int:pk>/', eliminarContratista, name='eliminarContratista'),
    path('detalle/<int:pk>/', detalleContratista, name='detalleContratista'),
    path('crearContrato/<int:pk>', crearContrato, name='crearContrato'),
    path('', LoginView.as_view(template_name='contratistas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)