from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('details/', views.detail, name='detail'),
    path('cadastro_prod/', views.cadastrar_produto, name='cadastro_prod')
]