from django import forms
from .models import Item, Movimentacao

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['item', 'tipo', 'quantidade', 'data_devolucao_prevista']
