from django import forms
from .models import Noticia, Bloco, Comunicado


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            "imagem",
            "imagem_destaque",
            "imagem_thumb",
            "imagem_noticia",
            "paragrafo",
        ]

        widgets = {
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
            "imagem_destaque": forms.FileInput(attrs={"class": "form-control"}),
            "imagem_thumb": forms.FileInput(attrs={"class": "form-control"}),
            "imagem_noticia": forms.FileInput(attrs={"class": "form-control"}),
            "paragrafo": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class BlocoForm(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ["imagem_bloco", "titulo_bloco", "paragrafo_bloco"]

        widgets = {
            "imagem_bloco": forms.FileInput(attrs={"class": "form-control"}),
            "titulo_bloco": forms.TextInput(attrs={"class": "form-control"}),
            "paragrafo_bloco": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }


class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ["titulo", "paragrafo"]
