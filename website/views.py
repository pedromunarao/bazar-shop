from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required



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
            return HttpResponse('Usuário já existente')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário Cadastrado com Sucesso')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, "index.html")
        else:
            return HttpResponse('Usuário ou Senha Inválidos')


def detail(request, pk):
    detalhes = get_object_or_404(Produto, pk=pk)
    return render(request, 'detail.html', {'produto': detalhes})


def cadastrar_produto(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.POST.get('nome', '')
        descricao = request.POST.get('descricao', '')
        preco = request.POST.get('preco', '')

        # Verifique se a chave 'imagem' existe no dicionário request.FILES

        imagem = request.FILES.get('imagem')

        # Crie um novo objeto de Produto com os dados do formulário
        novo_produto = Produto(titulo=nome, descricao=descricao, preco=preco, thumb=imagem)

        # Salve o objeto no banco de dados
        novo_produto.save()

        # Redirecione o usuário para uma página de sucesso ou outra página desejada
        # Neste exemplo, vamos redirecioná-lo de volta para a página de cadastro de produtos
        return render(request, 'cadastro_prod.html')

        # Se a requisição não for POST, apenas renderize o formulário de cadastro de produtos
    return render(request, 'cadastro_prod.html')


@login_required
def sair(request):
    logout(request)
    return redirect('index')


def compra(request, pk):
    compras = get_object_or_404(Produto, pk=pk)
    return render(request, 'checkout.html', {'produto': compras})





