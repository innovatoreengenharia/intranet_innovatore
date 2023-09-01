from django import forms
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies 



class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields =[ 
    'usuario','nome','sobrenome','nascimento','sexo','email', 'contato','cpf','rg','endereco','bairro','cidade','estado','numero', 'complemento','cargo_inicial','cargo', 'setor', 'cidade_trabalho', 'estado_trabalho', 'data_inicio', 'data_mudanca', 'email_empresa', 'telefone', 'obra_trabalho', 'texto_experiencia',
    ]

        widgets = {
            'nascimento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control data',
                    },
                ),
            'data_inicio': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control data'
                    },
                ),
            'data_mudanca': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control data'
                    },
                ),
            'sexo':forms.Select(
                attrs={
                    'class': 'form-control'
                    },
                ),
            'estado':forms.Select(
                attrs={
                    'class': 'form-control'
                    },
                ),
            'estado_trabalho':forms.Select(
                attrs={
                    'class': 'form-control'
                    },
                )
            
        }     

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields ='__all__'
        widgets = {

            'empresa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),

            'localidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),

            'forma_trabalho': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),

            'inicio_trabalho': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control data'
                    },
                ),

            'descricao_trabalho': forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),

            'termino_trabalho': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control data'
                    },
                ),
        } 

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields ='__all__'

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields ='__all__'

class HabilidadesForm(forms.ModelForm):
    class Meta:
        model = Habilidades
        fields ='__all__'


class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields ='__all__'

