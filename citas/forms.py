# from django import  forms
# from .models import Cita

# class CitaForm(forms.ModelForm):
#     class Meta:
#         model = Cita
#         fields = [
#             'clienteFK',
#             'eventoFK',
#             'fechaCita',
#             'horaCita',
#             'lugar',
#             'comentario'
#         ]

from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'clienteFK',
            'eventoFK',
            'fechaCita',
            'horaCita',
            'lugar',
            'comentario'
        ]
        labels = {
            'clienteFK': 'Cliente',
            'eventoFK': 'Evento',
            'fechaCita': 'Fecha de la cita',
            'horaCita': 'Hora de la cita',
            'lugar': 'Lugar de encuentro',
            'comentario': 'Comentarios adicionales'
        }
        widgets = {
            'clienteFK': forms.Select(attrs={
                'class': 'form-control',
            }),
            'eventoFK': forms.Select(attrs={
                'class': 'form-control',
            }),
            'fechaCita': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'horaCita': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'lugar': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Estudio fotográfico o domicilio del cliente'
            }),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe detalles adicionales sobre la cita...'
            }),
        }