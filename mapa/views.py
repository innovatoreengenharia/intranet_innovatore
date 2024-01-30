from django.shortcuts import render, redirect
from usuario.models import Perfil


def mapa(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    colaboradores_dexco = Perfil.objects.filter(obra_trabalho__icontains="dexco")
    
    context = {
        "perfil": perfil,
        "colaboradores_dexco": colaboradores_dexco,
    }

    return render(request, "mapa/mapa.html", context)
