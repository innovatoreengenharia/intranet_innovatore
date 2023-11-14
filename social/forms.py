from django import forms
from .models import Post, Comentarios

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'img', 'texto_postagem']
        widgets={

            'img': forms.FileInput(attrs={'class':'form-control' } ),

            'texto_postagem': forms.Textarea(attrs={'class': 'form-control'} ),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['user', 'texto_comentario', 'post']
        widgets={

            'texto_comentario': forms.Textarea(attrs={'class': 'form-control'} ),
        }

