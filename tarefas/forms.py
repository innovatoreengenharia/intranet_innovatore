from django import forms

from .models import Colunas, Quadros


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadros
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
        }


class ColunaForm(forms.ModelForm):
    class Meta:
        model = Colunas
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
        }
