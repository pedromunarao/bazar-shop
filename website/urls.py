from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('details/<int:pk>', views.detail, name='detail'),
    path('cadastro_prod/', views.cadastrar_produto, name='cadastro_prod'),
    path('deslogar/', views.sair),
    path('categoria/<int:categoria_id>/', views.produtos_por_categoria, name='categorias'),
    path('comprar/<int:produto_id>/', views.comprar_produto, name='comprar_produto'),
    path('confirmar/<int:compra_id>/', views.confirmar_compra, name='confirmar_compra'),
    path('minhas_compras/', views.minhas_compras, name='minhas_compras'),
    path('minhas_compras/<int:compra_id>/', views.minhas_compras, name='minhas_compras'),
    path('excluir_compra/<int:compra_id>/', views.excluir_compra, name='excluir_compra'),
    path('pesquisar_produto/', views.pesquisar_produto, name='pesquisar_produto'),
    path('meus_produtos/', views.meus_produtos, name='meus_produtos'),
    path('excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]
