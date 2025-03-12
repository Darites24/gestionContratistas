from django import forms
from .models import Contratista, Contrato


class ContratistaForm(forms.ModelForm):
    class Meta:
        model = Contratista
        fields = ['nombre','perfil','foto','direccion','telefono','profesion', 'nivel_educativo']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'perfil' : forms.TextInput(attrs={'class' : 'form-control'}),
            'foto' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'profesion' : forms.Select(attrs={'class' : 'form-control'}),
            'nivel_educativo' : forms.Select(attrs={'class' : 'form-control'})
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['contratista', 'fechaInicio', 'fechaFin', 'estado']
        widgets = {
            'contratista': forms.Select(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }