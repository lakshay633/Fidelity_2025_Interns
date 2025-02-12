from django import forms
from app_stocks.models import Stock

class ProductForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'