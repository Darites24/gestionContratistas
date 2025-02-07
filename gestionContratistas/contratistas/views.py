from django.shortcuts import render, get_object_or_404, redirect
from .models import Contratista, Contrato
from .forms import ContratistaForm, ContratoForm

def listarContratistas(request):
    contratistas = Contratista.objects.all()
    return render(request, 'contratistas/listar_Contratistas.html', {'contratistas':contratistas})


def crearContratista(request):
    if request.method == 'POST':
        form = ContratistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarContratistas')
    else:
        form = ContratistaForm()
    return render(request, 'contratistas/crear_Contratista.html', {'form':form})
    
    
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