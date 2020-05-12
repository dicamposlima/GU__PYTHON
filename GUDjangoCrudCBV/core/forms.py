from django import forms

from core.models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fieds = '__all__'
