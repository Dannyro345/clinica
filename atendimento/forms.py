from django.forms import ModelForm, TextInput
from .models import Cliente, Medico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_nasc': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'sexo': TextInput(attrs={'class':'form-control'}),
        }

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_nasc': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'sexo': TextInput(attrs={'class':'form-control'}),
        }