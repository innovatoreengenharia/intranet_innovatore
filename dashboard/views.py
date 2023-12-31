from django.shortcuts import render, redirect
from django.urls import reverse
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    mes_atual = timezone.now().month
    aniversariantes = Perfil.objects.filter(nascimento__month=mes_atual)

    aniversariantes_list = list(aniversariantes)
    shuffle(aniversariantes_list)

    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()

    if not perfil:
        return redirect('cadastro')

    context ={
        'perfil':perfil,
        'aniversariantes':aniversariantes_list,
    }

    return render(request, 'dashboard/home.html', context)
