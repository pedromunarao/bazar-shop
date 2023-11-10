from django.db import models
from django.db.models import Model
from django.utils import timezone
from django import forms
# Create your models here.

LISTA_CATEGORIAS = (
    ("SUPERIOR", "Parte Superior"),
    ("INFERIOR", "Parte Inferior"),
    ("UNICA", "Peça Única"),
    ("TER_PECA", "Terceira Peça"),
    ("ACESSORIOS", "Acessórios"),
    ("CALÇADO", "Calçado"),
    ("OUTROS", "Outros"),
)

'''
LISTA_SUBCATEGORIAS = (
    ("CAMISETA", "Camiseta"),
    ("REGATA", "Regata"),
    ("CROPPED", "Cropped"),
    ("CAMISA", "Camisa"),
    ("MOLETOM", "Moletom"),
    ("VESTIDO", "Vestido"),
    ("MACACAO", "Macacão"),
    ("SHORTS", "Shorts"),
    ("SAIA", "Saia"),
    ("CALCA", "Calça"),
    ("ANEL", "Anel"),
    ("PULSEIRA", "Pulseira"),
    ("COLAR", "Colar"),
    ("BRINCO", "Brinco"),
    ("TENIS", "Tênis"),
)
'''


class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='img_produto')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    # subcategoria = models.CharField(max_length=100, choices=LISTA_SUBCATEGORIAS)
    data_criacao = models.DateTimeField(default=timezone.now)
    preco = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.titulo






















