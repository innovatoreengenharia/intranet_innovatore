from django import forms
from .models import Noticia, Bloco, Comunicado, Quadro, Comentario_noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            "titulo",
            "imagem",
            "imagem_destaque",
            "imagem_thumb",
            "imagem_noticia",
            "paragrafo",
            "destaque",
            "tags",
        ]

        widgets = {
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "imagem_destaque": forms.FileInput(attrs={"class": "form-control"}),
            "imagem_thumb": forms.FileInput(attrs={"class": "form-control"}),
            "imagem_noticia": forms.FileInput(attrs={"class": "form-control"}),
            "paragrafo": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario_noticia
        fields = "__all__"


class BlocoForm(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ["imagem_bloco", "titulo_bloco", "paragrafo_bloco"]

        widgets = {
            "imagem_bloco": forms.FileInput(
                attrs={"class": "form-control imagem_bloco"}
            ),
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


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ["titulo", "paragrafo"]
