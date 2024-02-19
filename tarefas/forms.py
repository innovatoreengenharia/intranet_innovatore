from django import forms
from .models import Quadros


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadros
        fields = '__all__'
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
        }