from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import DadosCliente, MinhasFaturas
from .forms import DadosCalculoForm , UpFaturas,CustomUserCreationForm,DadosPessoaisForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'core/index.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado com Sucesso !!!")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)


def preenchimento(request):
    context = {
        'form':DadosCalculoForm(),
    }
   
    if request.method == 'POST':
        form = DadosCalculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'core/preenchimento.html', context)

def dados_pessoais(request):
    context = {
        'form':DadosPessoaisForm(),
    }
    if request.method == 'POST':
        form = DadosPessoaisForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'core/dados_pessoais.html', context)

def add_modal(request):
    return render(request, 'hx/add_modal.html')

def modalcalc1(request):
    return render(request, 'hx/modal_calc2.html')

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
 
 
def calculo(request,pk):
    dados = DadosCliente.objects.last()
    context = {
        'dados':dados
    }
    
    
    return render(request, 'core/calculo.html', context)

