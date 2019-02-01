from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Medico
from .forms import ClienteForm



# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html', {'clientes':clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/show.html', {'cliente':cliente})      

def cliente_form(request):
    if (request.method == 'POST'):
        form = ClienteForm(request.POST)
        form.save()
        return redirect('/atendimento/cliente/')     

    else:
        form = ClienteForm()
        return render(request, 'cliente/form.html', {'form':form})

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/list.html', {'medicos':medicos})

def medico_show(request, medico_id):
    medico = Medico.objects.get(pk=medico_id)
    return render(request, 'medico/show.html', {'medico':medico})      

