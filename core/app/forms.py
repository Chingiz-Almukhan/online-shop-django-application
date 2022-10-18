from django import forms
from django.shortcuts import get_object_or_404

from app.models import Product, ProductInCart


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск')


class AddEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost', 'image', 'category', 'qty']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Введите название', 'type': 'text', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Введите описание', 'type': 'text', 'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class AddEditCartForm(forms.ModelForm):
    class Meta:
        model = ProductInCart
        fields = ['qty']


