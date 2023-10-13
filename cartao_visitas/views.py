from django.shortcuts import render, redirect
from usuario.models import Perfil
from .models import Cartao_visitas 
from django.core.paginator import Paginator

def cartao_visitas(request):
    if not request.user.is_authenticated:
        return redirect('login')

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    cartoes = Cartao_visitas.objects.all()

    buscar_filtro = request.GET.get('buscar')
    if buscar_filtro:
        cartoes = Cartao_visitas.objects.filter(nome__contains=buscar_filtro)

    documento_paginator = Paginator(cartoes, 15)
    page_num = request.GET.get('page')
    page = documento_paginator.get_page(page_num)

    context = {
        'perfil': perfil,
        'page': page,
    }

    return render(request, 'cartao_visitas/cartao_visitas.html', context)