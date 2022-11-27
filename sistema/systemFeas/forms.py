from django import forms
from .models import bicicleta #Crar un form a partir de un modelo

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = bicicleta
        fields = '__all__'