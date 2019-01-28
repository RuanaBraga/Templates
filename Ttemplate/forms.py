
from django import forms
from .models  import cadastro

class Cadastro(forms.ModelForm):
     field_order = ['nome','telefone','cpf']

     class Meta:
         model = cadastro
         fields = '__all__'














