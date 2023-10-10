from django.shortcuts import render
from usuario.models import Perfil

def cursos(request):
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)

    context = {
        'perfil': perfil,
    }

    return render(request, 'cursos/cursos.html', context)
