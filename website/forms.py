from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'thumb', 'descricao', 'categoria', 'preco']

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        # Adiciona a classe 'form-control' aos campos para usar estilos do Bootstrap (opcional)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class ProdutoSearchForm(forms.Form):
    termo_pesquisa = forms.CharField(label='Pesquisar Produto', max_length=100)
