from django.shortcuts import render, redirect
from usuario.models import Perfil

def tarefas(request):
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()
    context = {
        'perfil': perfil,
    }
    return render(request, 'tarefas/tarefas.html', context)
