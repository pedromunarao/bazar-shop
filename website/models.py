from django.db import models
from django.db.models import Model
from django.utils import timezone
from django import forms
# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='img_produto')
    descricao = models.TextField(max_length=1000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.titulo























