from django.shortcuts import render, redirect
from usuario.models import Perfil


def mapa(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)

    # CEARÁ
    colaboradores_canadian = Perfil.objects.filter(obra_trabalho__icontains="canadian")

    # MARANHÃO -
    colaboradores_cibra = Perfil.objects.filter(obra_trabalho__icontains="cibra")

    # Pernanbuco
    colaboradores_nebras = Perfil.objects.filter(obra_trabalho__icontains="nebrás")


    colaboradores_ajinomoto = Perfil.objects.filter(obra_trabalho__icontains="ajinomoto")
    colaboradores_rousselot = Perfil.objects.filter(obra_trabalho__icontains="rousselot")
    colaboradores_agropalma = Perfil.objects.filter(obra_trabalho__icontains="agropalma")
    colaboradores_cobb = Perfil.objects.filter(obra_trabalho__icontains="cobb")
    colaboradores_meapler = Perfil.objects.filter(obra_trabalho__icontains="meapler")

    context = {
        "perfil": perfil,
        "colaboradores_canadian": colaboradores_canadian,
        "colaboradores_cibra": colaboradores_cibra,
        "colaboradores_nebras":colaboradores_nebras,
        "colaboradores_ajinomoto": colaboradores_ajinomoto,
        "colaboradores_rousselot": colaboradores_rousselot,
        "colaboradores_agropalma": colaboradores_agropalma,
        "colaboradores_cobb": colaboradores_cobb,
        "colaboradores_meapler": colaboradores_meapler,
    }

    return render(request, "mapa/mapa.html", context)
