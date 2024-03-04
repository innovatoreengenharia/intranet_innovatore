from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle
from django.db.models import Prefetch
from social.models import Post, Comentarios, Like
from social.forms import PostForm, ComentarioForm
import requests

# ip
def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_REMOTE_ADDR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Clima Tempo

import requests

def get_weather_data(request):
    api_key = '5184c8f1 ' 
    ip_user = get_ip(request)

    url = f"https://api.hgbrasil.com/weather?key={api_key}&user_ip={ip_user}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cidade =data['results']['city']
        temp = data['results']['temp']
        return data, cidade, temp, ip_user
    else:
        return None



def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
        
    data, cidade, temp, ip_user = get_weather_data(request)
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
        "cidade": cidade,
        "temp": temp,
    }
    return render(request, "dashboard/home.html", context)
