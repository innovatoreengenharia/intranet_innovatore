from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import PerfilForm, ExperienciaForm, FormacaoForm, CursosForm,HabilidadesForm, HobbiesForm
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies
from django.contrib import auth, messages
from PIL import Image


def cadastro(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        usuario_logado = request.user
        form = PerfilForm(request.user) 

        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm, extra=1)
        form_experiencia = form_experiencia_factory()
        context = {
             'form': form,
             'form_experiencia': form_experiencia,
             'usuario_logado':usuario_logado,
             }
        return render(request, 'usuario/form.html', context)
    
    elif request.method == 'POST':
        form = PerfilForm(request.POST)
        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm)
        form_experiencia = form_experiencia_factory(request.POST)

        if form.is_valid() and form_experiencia.is_valid():
            formulario_pai = form.save()
            form_experiencia.instance = formulario_pai
            return redirect(reverse('usuario/perfil.html'))

        else:
            context = {
                 'form': form,
                 'form_sobre ': form_sobre,
                 'form_experiencia':form_experiencia,
            }
            return render(request, 'usuario/form.html', context)

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    usuario_logado = request.user
    
    
    perfil_usuario = Perfil.objects.get(usuario = usuario_logado)
    context = {
        'perfil_usuario': perfil_usuario,
    }
    return render(request,'usuario/perfil.html')
