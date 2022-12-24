from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosCliente, MinhasFaturas
from .forms import DadosCalculoForm , UpFaturas

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def preenchimento(request):
    context = {
        'form':DadosCalculoForm(),
    }
    if request.method == 'POST':
        form = DadosCalculoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'core/preenchimento.html', context)

def dados_pessoais(request):
    context = {
        'form':DadosCalculoForm(),
    }
    if request.method == 'POST':
        form = DadosCalculoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'core/dados_pessoais.html', context)

def add_modal(request):
    return render(request, 'hx/add_modal.html')

def upfatura(request):
    context = {
        'up':UpFaturas(),
    }
    if request.method == "GET":
        return render(request, "core/upfaturas.html",context)
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        
        mf = MinhasFaturas(title= "minha_imagem", arq=file)
        mf.save()
        return render(request, "core/upfaturas.html",context)
 


