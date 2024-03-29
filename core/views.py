from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import DadosCliente, MinhasFaturas,DadosPessoais
from .forms import DadosCalculoForm , UpFaturas,CustomUserCreationForm,DadosPessoaisForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# @login_required
@csrf_exempt
def index(request):
    return render(request, 'core/index.html')

@csrf_exempt
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

@csrf_exempt
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


@csrf_exempt
def dados_pessoais(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        print(nome)
        email = request.POST.get("email")
        empresa = request.POST.get("empresa")
        telefone = request.POST.get("telefone")
        form = DadosPessoais.objects.create(nome=nome,email=email,empresa=empresa,telefone=telefone)
        form.save()
        return redirect('calculo')
    return render(request,'core/dados_pessoais.html')

def add_modal(request):
    return render(request, 'hx/add_modal.html')

def modalcalc1(request):
    return render(request, 'hx/modal_calc2.html')

@csrf_exempt
def upfatura(request):
    context = {
        'up':UpFaturas(),
    }
    if request.method == "GET":
        return render(request, "core/upfaturas.html",context)
    elif request.method == "POST":
        titulo = request.POST.get("minha_imagem")
        file = request.FILES.get("meu_arq")
        print(file)
        
        mf = MinhasFaturas(titulo= "minha_imagem", arquivo = file)
        mf.save()
        return redirect('index')
 
@csrf_exempt
def calculo(request):
    dados = DadosCliente.objects.last()
    context = {
        'dados':dados
    }
    
    return render(request, 'core/calculo.html', context)

