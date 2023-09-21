from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .forms import PerfilForm, ExperienciaForm, FormacaoForm, CursosForm,HabilidadesForm, HobbiesForm
from .models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies
from datetime import date
from django.contrib import auth, messages
from PIL import ImageChops

def cadastro(request):
    usuario_id = request.user.id
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        usuario_logado = request.user
        usuario_id = request.user.id
        form = PerfilForm() 


        context = {
             'form': form,
             'usuario_logado': usuario_logado,
             'usuario_id': usuario_id,
             
             }
        return render(request, 'usuario/form.html', context)
    
    elif request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)


        if form.is_valid():
            form.save()

            return redirect(reverse('home'))

        else:
            context = {
                 'form': form,
            }
            print('ERRO NO CADASTRO', form.errors, usuario_id)
            return render(request, 'usuario/form.html', context)

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    usuario_logado = request.user
    logado_id = request.user.id
    hoje = date.today()
    
    query_usuario = Perfil.objects.filter(usuario_id = logado_id)

    try:
        perfil_usuario = query_usuario[0]
        id_perfil = perfil_usuario.id
        experiencia = Experiencia.objects.filter(perfil_id = id_perfil)
        formacao = Formacao.objects.filter(perfil_id = id_perfil)
        cursos = Cursos.objects.filter(perfil_id = id_perfil)
        habilidades = Habilidades.objects.filter(perfil_id = id_perfil)
        hobbies = Hobbies.objects.filter(perfil_id = id_perfil)
        context = {
            'perfil': perfil_usuario,
            'usuario_logado': usuario_logado,
            'logado_id': logado_id,
            'experiencia': experiencia,
            'formacao': formacao,
            'cursos': cursos,
            'habilidades':habilidades,
            'hobbies': hobbies,
            'hoje': hoje,
        }
        return render(request,'usuario/perfil.html',context)
    except:
        print('erro no perfil')
        return redirect('cadastro')

def editPerfil (request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    if(request.method == 'GET'):
        usuario_logado = request.user
        usuario_id = request.user.id
        perfil = Perfil.objects.filter(pk=id).first()

        if perfil is None:
            return redirect(reverse('cadastro'))
        
        form = PerfilForm(instance=perfil)

        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm, extra=1)
        form_experiencia = form_experiencia_factory(instance=perfil)

        form_formacao_factory = inlineformset_factory(Perfil, Formacao, form=FormacaoForm, extra=1)
        form_formacao = form_formacao_factory(instance=perfil)

        form_cursos_factory = inlineformset_factory(Perfil, Cursos, form=CursosForm, extra=1)
        form_cursos = form_cursos_factory(instance=perfil)

        form_habilidades_factory = inlineformset_factory(Perfil, Habilidades, form=HabilidadesForm, extra=1)
        form_habilidades = form_habilidades_factory(instance=perfil)

        form_hobbies_factory = inlineformset_factory(Perfil, Hobbies, form=HobbiesForm, extra=1)
        form_hobbies = form_hobbies_factory(instance=perfil)

        context = {
            'usuario': usuario_logado,
            'usuario_id': usuario_id,
            'form': form, 
            'perfil': perfil,
            'form_experiencia':form_experiencia,
            'form_formacao': form_formacao,
            'form_cursos': form_cursos,
            'form_habilidades': form_habilidades,
            'form_hobbies': form_hobbies,
        }
        return render(request, 'usuario/editar_perfil.html', context)

    elif(request.method == 'POST'):
        perfil = Perfil.objects.filter(pk=id).first()
        usuario_id = request.user.id
        if perfil is None:
            return redirect(reverse('cadastro'))
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        form_experiencia_factory = inlineformset_factory(Perfil, Experiencia, form=ExperienciaForm)
        form_experiencia = form_experiencia_factory(request.POST, instance=perfil)

        form_formacao_factory = inlineformset_factory(Perfil, Formacao, form=FormacaoForm)
        form_formacao = form_formacao_factory(request.POST, instance=perfil)

        form_cursos_factory = inlineformset_factory(Perfil, Cursos, form=CursosForm)
        form_cursos = form_cursos_factory(request.POST, instance=perfil)

        form_habilidades_factory = inlineformset_factory(Perfil, Habilidades, form=HabilidadesForm)
        form_habilidades = form_habilidades_factory(request.POST, instance=perfil)

        form_hobbies_factory = inlineformset_factory(Perfil, Hobbies, form=HobbiesForm)
        form_hobbies = form_hobbies_factory(request.POST, instance=perfil)

        if (form.is_valid() 
                and form_experiencia.is_valid()
                and form_formacao.is_valid()
                and form_cursos.is_valid()
                and form_habilidades.is_valid()
                and form_hobbies.is_valid()
                ):
            principal = form.save()
            form_experiencia.instance = principal
            form_formacao.instance = principal
            form_cursos.instance = principal
            form_habilidades.instance = principal
            form_hobbies.instance = principal

            form_experiencia.save()
            form_formacao.save()
            form_cursos.save()
            form_habilidades.save()
            form_hobbies.save()

            return redirect('perfil')
        else:
            context={
                'form': form,
                'perfil': perfil,
                'usuario_id': usuario_id,
                'form_experiencia': form_experiencia,
                'form_formacao':form_formacao,
                'form_cursos':form_cursos,
                'form_habilidades': form_habilidades,
                'form_hobbies': form_hobbies,
            }
            print('ERRO NO EDIT', 
                  'Form',form.is_valid(), form.errors,
                  'exp',form_experiencia.is_valid(), form_experiencia.errors,
                  'formacao',form_formacao.is_valid(), form_formacao.errors,
                  'cursos',form_cursos.is_valid(), form_cursos.errors,
                  'hab',form_habilidades.is_valid(), form_habilidades.errors,
                  'hob',form_hobbies.errors,form_hobbies.errors,
                )
            return render(request, 'usuario/editar_perfil.html', context)
        


def deletar_experiencia(request, id ):
    experiencia = Experiencia.objects.get(pk=id)
    experiencia.delete()
    return redirect('perfil')

def deletar_formacao(request, id ):
    formacao = Formacao.objects.get(pk=id)
    formacao.delete()
    return redirect('perfil')

def deletar_curso(request, id ):
    curso = Cursos.objects.get(pk=id)
    curso.delete()
    return redirect('perfil')

def deletar_habilidade(request, id ):
    habilidade = Habilidades.objects.get(pk=id)
    habilidade.delete()
    return redirect('perfil')

def deletar_hobbie(request, id ):
    usuario_id = request.user.id
    hobbie = Hobbies.objects.get(pk=id)
    hobbie.delete()
    return redirect('perfil')

