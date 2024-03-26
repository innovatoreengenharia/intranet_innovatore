from django.shortcuts import redirect, render

from usuario.models import Perfil


def mapa(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)

    # MARANHÃO -
    colaboradores_cibra = Perfil.objects.filter(
        obra_trabalho__icontains="cibra"
    ).order_by("?")
    # SÃO PAULO
    colaboradores_zortea = Perfil.objects.filter(
        obra_trabalho__icontains="zortea"
    ).order_by("?")

    colaboradores_ajinomoto = Perfil.objects.filter(
        obra_trabalho__icontains="ajinomoto"
    ).order_by("?")

    colaboradores_rousselot = Perfil.objects.filter(
        obra_trabalho__icontains="rousselot"
    ).order_by("?")

    colaboradores_agropalma = Perfil.objects.filter(
        obra_trabalho__icontains="agropalma"
    ).order_by("?")

    colaboradores_cobb = Perfil.objects.filter(
        obra_trabalho__icontains="cobb"
    ).order_by("?")

    colaboradores_meapler = Perfil.objects.filter(
        obra_trabalho__icontains="meapler"
    ).order_by("?")

    colaboradores_gps = Perfil.objects.filter(
        obra_trabalho__icontains="gps"
    ).order_by("?")

    colaboradores_sede = Perfil.objects.filter(
        obra_trabalho__icontains="sede"
    ).order_by("?")

    # colaboradores_grand = Perfil.objects.filter(
    #     obra_trabalho__icontains="grand"
    # )

    # RIO GRANDE DO SUL
    colaboradores_yara = Perfil.objects.filter(obra_trabalho__icontains="yara")

    context = {
        "perfil": perfil,
        "colaboradores_cibra": colaboradores_cibra,
        "colaboradores_sede": colaboradores_sede,
        "colaboradores_zortea": colaboradores_zortea,
        "colaboradores_ajinomoto": colaboradores_ajinomoto,
        "colaboradores_rousselot": colaboradores_rousselot,
        "colaboradores_agropalma": colaboradores_agropalma,
        "colaboradores_cobb": colaboradores_cobb,
        "colaboradores_meapler": colaboradores_meapler,
        "colaboradores_gps": colaboradores_gps,
        # "colaboradores_grand": colaboradores_grand,
        "colaboradores_yara": colaboradores_yara,
    }

    return render(request, "mapa/mapa.html", context)
