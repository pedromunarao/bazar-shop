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
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('checkout/<int:pk>', views.compra, name='compra')
]
