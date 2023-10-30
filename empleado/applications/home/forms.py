from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
        )
        widgets = {
            'titulo': forms.TextInput( #para numero es NumberImput
                attrs = { #hacemos la personalizacion del input 
                    'placeholder':'Ingrese texto aqui'
                }
            )
        }

        #validacion
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if titulo < 'sara':
            raise forms.ValidationError('El titulo que debe ingresar es "sara" ')
            
        return titulo
