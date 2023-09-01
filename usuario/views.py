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
        nome = request.user.first_name
        sobrenome = request.user.last_name
        usuario_id = request.user.id
        form = PerfilForm() 

        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm, extra=1)
        form_experiencia = form_experiencia_factory()
        context = {
             'form': form,
             'form_experiencia': form_experiencia,
             'usuario_logado': usuario_logado,
             'usuario_id': usuario_id,
             'nome': nome,
             'sobrenome': sobrenome,
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
            print('ERROR NO CADASTRO', form.is_valid(), form_experiencia.is_valid(), form.errors, form_experiencia.errors)
            return render(request, 'usuario/form.html', context)

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    usuario_logado = request.user
    logado_id = request.user.id
    
    query_usuario = Perfil.objects.filter(usuario_id = logado_id)

    try:
        perfil_usuario = query_usuario[0]

        id_perfil = perfil_usuario.id
        experiencia = Experiencia.objects.filter(perfil_id = id_perfil)
        context = {
            'pu': perfil_usuario,
            'usuario_logado': usuario_logado,
            'logado_id': logado_id,
            'experiencia': experiencia,
        }
        return render(request,'usuario/perfil.html',context)
    except:
        return redirect('cadastro')

def editPerfil (request, id):
    if(request.method == 'GET'):
        usuario_logado = request.user
        usuario_id = request.user.id
        perfil = Perfil.objects.filter(pk=id).first()
        if perfil is None:
            return redirect(reverse('cadastro'))
        form = PerfilForm(instance=perfil)
        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm, extra=1)
        form_experiencia = form_experiencia_factory(instance=perfil)
        context = {
            'usuario': usuario_logado,
            'usuario_id': usuario_id,
            'form': form, 
            'perfil': perfil,
            'form_experiencia':form_experiencia,
        }
        return render(request, 'usuario/editar_perfil.html', context)

    elif(request.method == 'POST'):
        perfil = Perfil.objects.filter(pk=id).first()
        if perfil is None:
            return redirect(reverse('cadastro'))
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm)
        form_experiencia = form_experiencia_factory(request.POST, instance=perfil)

        if form.is_valid() and form_experiencia.is_valid():
            principal = form.save()
            form_experiencia.instance = principal
            form_experiencia.save()
            return redirect('perfil')
        else:
            context={
                'form': form,
                'perfil': perfil,
                'form_experiencia': form_experiencia,
            }
            print('ERRO NO EDIT', form.is_valid(), form_experiencia.is_valid(), form.errors, form_experiencia.errors)
            return render(request, 'usuario/editar_perfil.html', context)

