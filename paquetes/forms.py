from django import forms
from .models import Paquete

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['nombrePaquete', 'descripcionPaquete', 'precio']