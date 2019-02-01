from django.forms import ModelForm
from .models import Cliente, Medico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'