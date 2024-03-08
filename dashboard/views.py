import datetime
from random import shuffle

import requests
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from informativos.models import Noticia
from social.forms import ComentarioForm, PostForm
from social.models import Comentarios, Like, Post
from usuario.models import Perfil

# ESTAÇÕES DO ANO


def estacao_do_ano(data):
    if (
        (data.month == 3 and data.day >= 20)
        or (data.month == 4)
        or (data.month == 5)
        or (data.month == 6 and data.day < 21)
    ):
        return "Outono"
    elif (
        (data.month == 6 and data.day >= 21)
        or (data.month == 7)
        or (data.month == 8)
        or (data.month == 9 and data.day < 23)
    ):
        return "Inverno"
    elif (
        (data.month == 9 and data.day >= 23)
        or (data.month == 10)
        or (data.month == 11)
        or (data.month == 12 and data.day < 21)
    ):
        return "Primavera"
    elif (
        (data.month == 12 and data.day >= 21)
        or (data.month == 1)
        or (data.month == 2)
        or (data.month == 3 and data.day < 20)
    ):
        return "Verão"
    else:
        return "Erro: Data fora do intervalo de datas das estações do ano."


# API HG Brasil
def get_weather_data(city_name, state):
    api_key = "5184c8f1"

    url = f"https://api.hgbrasil.com/weather?key={api_key}&city_name={city_name},{state}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cidade = data["results"]["city"]
        temp = data["results"]["temp"]
        condition_slug = (
            f"dashboard/img/{data['results']['condition_slug']}.svg"
        )
        print(f"Condição=== {condition_slug}")
        return data, cidade, temp, condition_slug
    else:
        data = ""
        cidade = "Limeira"
        temp = "--"
        condition_slug = "dashboard/img/clear_day.svg"

        return data, cidade, temp, condition_slug


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = request.user.id
    try:
        perfil = Perfil.objects.get(usuario_id=id_usuario)
    except:
        perfil = None

    if not perfil:
        return redirect("cadastro")

    mes_atual = timezone.now().month
    aniversariantes = Perfil.objects.filter(nascimento__month=mes_atual)

    aniversariantes_list = list(aniversariantes)
    shuffle(aniversariantes_list)

    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    postagens = Post.objects.order_by("-criado_em")[:10].prefetch_related(
        Prefetch(
            "comentarios_set",
            queryset=Comentarios.objects.order_by("criado_em"),
        ),
        Prefetch("like_set", queryset=Like.objects.all()),
    )
    user_likes = [
        item.post.id for item in Like.objects.filter(user_id=id_usuario)
    ]

    if perfil.cidade_trabalho:
        city_name = perfil.cidade_trabalho
    else:
        city_name = "Limeira"

    if perfil.estado_trabalho:
        state = perfil.estado_trabalho
    else:
        state = ""

    # buscar Cidade
    buscar_cidade = request.GET.get("buscar_cidade")
    buscar_estado = request.GET.get("buscar_estado")

    if buscar_cidade and buscar_estado:
        city_name = buscar_cidade
        state = buscar_estado

    _, cidade, temp, condition_slug = get_weather_data(city_name, state)

    # ESTAÇOES DO ANO

    data_atual = datetime.date.today()
    estacao = estacao_do_ano(data_atual)

    # informativos
    noticia = Noticia.objects.last()

    context = {
        "perfil": perfil,
        "aniversariantes": aniversariantes_list,
        "usuarios": usuarios,
        "noticia": noticia,
        "postagens": postagens,
        "user_likes": user_likes,
        "cidade": cidade,
        "temp": temp,
        "estacao": estacao,
        "condicao": condition_slug,
    }
    return render(request, "dashboard/home.html", context)
