from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'telefono', 'tipo_proyecto', 'presupuesto', 'mensaje', 'fuente']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 5}),
        }