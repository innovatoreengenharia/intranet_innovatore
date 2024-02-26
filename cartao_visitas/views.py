from django.shortcuts import render, redirect
from usuario.models import Perfil
from .models import Cartao_visitas
from django.core.paginator import Paginator
from django.db.models import Q
import pandas as pd

def importar_dados_do_excel():
    caminho_arquivo ="/usr/src/app/cartao_visitas/cartoes.xlsx"
    # Ler o arquivo Excel
    dados_excel = pd.read_excel(caminho_arquivo)

    # Iterar sobre as linhas do DataFrame
    for index, linha in dados_excel.iterrows():
        # Criar uma instância do modelo Cartao_visitas
        cartao = Cartao_visitas(
            nome=linha['NOME'],
            empresa=linha['EMPRESA'],
            email=linha['E-MAIL'],
            telefone_fixo=linha['TELEFONE FIXO'],
            telefone_celular=linha['TELEFONE CELULAR'],
            site=linha['SITE']
        )
        # Salvar a instância no banco de dados
        cartao.save()


def cartao_visitas(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    cartoes = Cartao_visitas.objects.all()

    buscar_filtro = request.GET.get("buscar")
    if buscar_filtro:
        cartoes = Cartao_visitas.objects.filter(
            Q(nome__icontains=buscar_filtro)
            | Q(empresa__icontains=buscar_filtro)
            | Q(email__icontains=buscar_filtro)
            | Q(site__icontains=buscar_filtro)
        )

    documento_paginator = Paginator(cartoes, 50)
    page_num = request.GET.get("page")
    page = documento_paginator.get_page(page_num)

    context = {
        "buscar": buscar_filtro,
        "perfil": perfil,
        "page": page,
    }

    return render(request, "cartao_visitas/cartao_visitas.html", context)
