from django.shortcuts import render, redirect
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle

def aniversariantes(request):

    if not request.user.is_authenticated:
        return redirect('login')

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    mes_atual = timezone.now().month
    aniversariantes = Perfil.objects.filter(nascimento__month=mes_atual)

    aniversariantes_list = list(aniversariantes)
    shuffle(aniversariantes_list)

    context = {
        "perfil":perfil,
        "aniversariantes": aniversariantes_list,
    }

    return render(request, 'aniversariantes/aniversariantes.html', context)
