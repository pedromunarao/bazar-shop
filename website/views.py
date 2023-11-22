from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from .models import Produto, Categoria, Compra
from .forms import ProdutoForm, ProdutoSearchForm, CompraForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, "index.html")


def shop(request):
    produtos = Produto.objects.all()

    # Configuração da paginação
    paginator = Paginator(produtos, 6)  # 6 produtos por página
    page = request.GET.get('page')

    try:
        produtos_paginados = paginator.page(page)
    except PageNotAnInteger:
        produtos_paginados = paginator.page(1)
    except EmptyPage:
        produtos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', {'produtos': produtos_paginados})


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
            produto.usuario = request.user
            produto.save()
            messages.success(request, "Produto cadastrado com sucesso")
            return redirect('meus_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'cadastro_prod.html', {'form': form})


@login_required
def sair(request):
    logout(request)
    messages.warning(request, "Usuário deslogado")
    return HttpResponseRedirect('/')


def produtos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'produtos': produtos,
    }

    return render(request, 'categorias.html', context)


@login_required
def comprar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.produto = produto
            compra.save()
            # messages.success(request, 'Compra Realizada com Sucesso!')
            return redirect('confirmar_compra', compra_id=compra.id)
    else:
        form = CompraForm()

    return render(request, 'minhas_compras.html', {'produto': produto, 'form': form})


@login_required
def confirmar_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    return render(request, 'confirmar_compra.html', {'compra': compra})


@login_required
def minhas_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    return render(request, 'minhas_compras.html', {'compras': compras})


@login_required
def excluir_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)

    if request.method == 'POST':
        compra.delete()
        return redirect('minhas_compras')

    return render(request, 'excluir_compra.html', {'compra': compra})


def pesquisar_produto(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.filter(titulo__icontains=query)
    return render(request, 'pesquisar_produto.html', {'produtos': produtos, 'query': query})


@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, usuario=request.user)

    # Lógica de exclusão
    produto.delete()

    return JsonResponse({'message': 'Produto excluído com sucesso'})


@login_required
def meus_produtos(request):
    produtos = Produto.objects.filter(usuario=request.user)
    return render(request, 'meus_produtos.html', {'produtos': produtos})

