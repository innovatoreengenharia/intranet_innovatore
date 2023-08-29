from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .forms import PerfilForm, ExperienciaForm, FormacaoForm, CursosForm,HabilidadesForm, HobbiesForm
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies
from django.contrib import auth, messages
from PIL import ImageChops

def cadastro(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        usuario_logado = request.user
        usuario_id = request.user.id
        form = PerfilForm() 

        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm, extra=1)
        form_experiencia = form_experiencia_factory()
        context = {
             'form': form,
             'form_experiencia': form_experiencia,
             'usuario_logado': usuario_logado,
             'usuario_id': usuario_id,
             }
        return render(request, 'usuario/form.html', context)
    
    elif request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm)
        form_experiencia = form_experiencia_factory(request.POST)


        if form.is_valid() and form_experiencia.is_valid():
            perfil = form.save()
            form_experiencia.instance = perfil
            form_experiencia.save()

            return redirect(reverse('perfil'))

        else:
            context = {
                 'form': form,
                 'form_experiencia':form_experiencia,
            }
            print('ERROR DU CARALHO',form.errors)
            return render(request, 'usuario/form.html', context)

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    usuario_logado = request.user
    logado_id = request.user.id
    
    
    query_usuario = Perfil.objects.filter(usuario_id = logado_id)
    perfil_usuario = query_usuario[0]
    context = {
        'pu': perfil_usuario,
        'usuario_logado':usuario_logado,
        'logado_id':logado_id,
    }
    return render(request,'usuario/perfil.html',context)

def editPerfil (request, id):
    perfil = get_object_or_404(Perfil, pk=id)
    form = PerfilForm(instance=perfil)
    if(request.method == 'GET'):
        return render(request, 'usuario/editar_perfil.html', {'form': form, 'perfil': perfil})

    elif(request.method == 'POST'):
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            perfil.save()
            return redirect('perfil')
        else:
            return render(request, 'usuario/editar_perfil.html', {'form': form, 'perfil': perfil})

