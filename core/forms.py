from django import forms
from .models import DadosCliente , MinhasFaturas,DadosPessoais

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DadosCalculoForm(forms.ModelForm):
    class Meta:
        model = DadosCliente
        fields ='__all__'
        
class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields ='__all__'
        
class UpFaturas(forms.ModelForm):
    class Meta:
        model = MinhasFaturas
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
        model = User
        fields = ['username',"first_name", "last_name", "email", "password1", "password2"]
    