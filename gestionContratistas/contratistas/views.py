from django.shortcuts import render, get_object_or_404, redirect
from .models import Contratista, Contrato
from .forms import ContratistaForm, ContratoForm
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas

def listarContratistas(request):
    contratistas = Contratista.objects.all()
    return render(request, 'contratistas/listar_Contratistas.html', {'contratistas':contratistas})


def crearContratista(request):
    if request.method == 'POST':
        form = ContratistaForm(request.POST, request.FILES)
        if form.is_valid():
            contratista = form.save()
            salario = contratista.nivel_educativo.honorarios
            contrato_pdf = generarContratoPdf(contratista, salario)
            response = HttpResponse(contrato_pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Contrato_{contratista.nombre}"'
            return response
    else:
        form = ContratistaForm()
    return render(request, 'contratistas/crear_Contratista.html', {'form':form})
    

def generarContratoPdf(contratista, salario):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Contrato de: {contratista.nombre}")
    p.drawString(100, 700, f"Profesión: {contratista.profesion.nombre}")
    p.drawString(100, 650, f"Nivel Educativo: {contratista.nivel_educativo.nombre}")
    p.drawString(100, 600, f"Salario: {salario}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
    

def editarContratista(request, pk):
    contratista = get_object_or_404(Contratista, pk=pk)
    if request.method == 'POST':
        form = ContratistaForm(request.POST, request.FILES, instance=contratista)
        if form.is_valid():
            form.save()
            return redirect('listarContratistas')
    else:
        form = ContratistaForm(instance=contratista)
    return render(request, 'contratistas/editar_Contratista.html', {'form': form})

def eliminarContratista(request, pk):
    contratista = get_object_or_404(Contratista, pk=pk)
    if request.method == 'POST':
        contratista.delete()
        return redirect('listarContratistas')
    return render(request, 'contratistas/eliminar_Contratista.html', {'contratista': contratista})

def detalleContratista(request, pk):
    contratista = get_object_or_404(Contratista, pk=pk)
    return render(request, 'contratistas/detalle_Contratista.html', {'contratista' : contratista})