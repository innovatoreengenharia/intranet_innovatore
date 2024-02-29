from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle
from django.db.models import Prefetch
from social.models import Post, Comentarios, Like
from social.forms import PostForm, ComentarioForm

# Clima Tempo

import requests

# def get_weather_data():
#     api_key = '5184c8f1 '
#     # url = f'https://api.hgbrasil.com/weather?key={api_key}' 

#     url = f"https://api.hgbrasil.com/weather?key={api_key}&user_ip=remote"

#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         cidade =data['results']['city']
#         temp =f"{data['results']['temp']}º"
#         print("TENTATIVA DE CIDADE", cidade, temp)
#         return data, cidade, temp
#     else:
#         print("DEU RUIM!!!!!!!!!!!!!!!!")
#         return None



def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
        
    # data, cidade, temp = get_weather_data()
    id_usuario = request.user.id
    try:
        perfil = Perfil.objects.get(usuario_id=id_usuario)
    except:
        perfil = None

    mes_atual = timezone.now().month
    aniversariantes = Perfil.objects.filter(nascimento__month=mes_atual)

    aniversariantes_list = list(aniversariantes)
    shuffle(aniversariantes_list)

    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    postagens = Post.objects.order_by("-criado_em")[:10].prefetch_related(
        Prefetch("comentarios_set", queryset=Comentarios.objects.order_by("criado_em")),
        Prefetch("like_set", queryset=Like.objects.all()),
    )
    user_likes = [item.post.id for item in Like.objects.filter(user_id=id_usuario)]

    if not perfil:
        return redirect("cadastro")

    context = {
        "perfil": perfil,
        "aniversariantes": aniversariantes_list,
        "usuarios": usuarios,
        "postagens": postagens,
        "user_likes": user_likes,
        # "cidade": cidade,
        # "temp": temp,
    }
    return render(request, "dashboard/home.html", context)
