from django.shortcuts import render
from usuario.models import Perfil
from .models import Cartao_visitas 

def cartao_visitas(request):
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    cartoes = Cartao_visitas.objects.all()

    context = {
        'perfil': perfil,
        'cartoes':cartoes,
    }

    return render(request, 'cartao_visitas/cartao_visitas.html', context)