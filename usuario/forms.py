from django import forms
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies 



class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields ='__all__'
    def __init__(self, user=None, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields ='__all__'

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

