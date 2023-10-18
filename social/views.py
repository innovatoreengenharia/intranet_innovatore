from django.shortcuts import render, redirect
from usuario.models import Perfil

def social(request):

    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)

    context = {
        "perfil":perfil,
    }
    return render(request, 'social/social.html', context)


def contatos(request):

    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)

    context = {
        "perfil":perfil,
    }

    return render(request, 'social/contatos.html', context)