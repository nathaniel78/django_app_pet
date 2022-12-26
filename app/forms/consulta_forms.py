from .django import forms
from .models import ConsultaPet

class ConsultaPetForm(forms.ModelForm):
    class meta:
        model = ConsultaPet
        fields = '__all__'
        exclude = ['pet', 'data']