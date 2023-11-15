from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from .models import Produto
from .forms import ProdutoForm, ProdutoSearchForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def shop(request):
    produtos = Produto.objects.all()
    return render(request, "shop.html", {'produtos': produtos})


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            messages.warning(request, "Usuário já existente")
            return render(request, 'login.html')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, "Usuário cadastrado com Sucesso")

        return render(request, 'login.html')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            messages.success(request, "Logado com sucesso")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return HttpResponseRedirect('/login')


def detail(request, pk):
    detalhes = get_object_or_404(Produto, pk=pk)
    return render(request, 'detail.html', {'produto': detalhes})



@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.data_criacao = timezone.now()
            produto.save()
            messages.success(request, "Produto cadastrado com sucesso")
            return redirect('shop')
    else:
        form = ProdutoForm()

    return render(request, 'cadastro_prod.html', {'form': form})


@login_required
def sair(request):
    logout(request)
    messages.warning(request, "Usuário deslogado")
    return HttpResponseRedirect('/')


def compra(request, pk):
    compras = get_object_or_404(Produto, pk=pk)
    return render(request, 'checkout.html', {'produto': compras})


def pesquisa_produto(request):
    if request.method == 'GET':
        form = ProdutoSearchForm(request.GET)
        if form.is_valid():
            termo_pesquisa = form.cleaned_data['termo_pesquisa']
            produtos = Produto.objects.filter(nome__icontains=termo_pesquisa)
        else:
            produtos = Produto.objects.all()
    else:
        form = ProdutoSearchForm()
        produtos = Produto.objects.all()

    return render(request, 'sua_app/pesquisa_produto.html', {'form': form, 'produtos': produtos})





