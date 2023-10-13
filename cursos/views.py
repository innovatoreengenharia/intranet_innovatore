from django.shortcuts import render, redirect
from usuario.models import Perfil
from .models import Cursos

def cursos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)

    cursos = Cursos.objects.order_by('-data')

    context = {
        'perfil': perfil,
        'cursos': cursos,
    }

    return render(request, 'cursos/cursos.html', context)
