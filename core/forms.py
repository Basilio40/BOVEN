from django import forms
from .models import DadosCliente , MinhasFaturas

class DadosCalculoForm(forms.ModelForm):
    class Meta:
        model = DadosCliente
        fields ='__all__'
        
class UpFaturas(forms.ModelForm):
    class Meta:
        model = MinhasFaturas
        fields = '__all__'