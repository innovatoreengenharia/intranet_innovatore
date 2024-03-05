from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle
from django.db.models import Prefetch
from social.models import Post, Comentarios, Like
from social.forms import PostForm, ComentarioForm
import datetime
import requests

#ESTAÇÕES DO ANO

def estacao_do_ano(data):
    if (data.month == 3 and data.day >= 20) or (data.month == 4) or (data.month == 5) or (data.month == 6 and data.day < 21):
        return "Outono"
    elif (data.month == 6 and data.day >= 21) or (data.month == 7) or (data.month == 8) or (data.month == 9 and data.day < 23):
        return "Inverno"
    elif (data.month == 9 and data.day >= 23) or (data.month == 10) or (data.month == 11) or (data.month == 12 and data.day < 21):
        return "Primavera"
    elif (data.month == 12 and data.day >= 21) or (data.month == 1) or (data.month == 2) or (data.month == 3 and data.day < 20):
        return "Verão"
    else:
        return "Erro: Data fora do intervalo de datas das estações do ano."

# API HG Brasil
def get_weather_data(city_name, state):
    api_key = '5184c8f1' 

    url = f"https://api.hgbrasil.com/weather?key={api_key}&city_name={city_name},{state}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cidade =data['results']['city']
        temp = data['results']['temp']
        return data, cidade, temp
    else:
        data = ""
        cidade = "Limeira"
        temp = '--'
        return data, cidade, temp



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
        Prefetch("comentarios_set", queryset=Comentarios.objects.order_by("criado_em")),
        Prefetch("like_set", queryset=Like.objects.all()),
    )
    user_likes = [item.post.id for item in Like.objects.filter(user_id=id_usuario)]

    if perfil.cidade_trabalho:
        city_name = perfil.cidade_trabalho
    else:
        city_name = "Limeira" 

    if perfil.estado_trabalho:
        state = perfil.estado_trabalho
    else:
        state = ""

    data, cidade, temp = get_weather_data(city_name, state)

    #ESTAÇOES DO ANO

    data_atual = datetime.date.today()
    estacao = estacao_do_ano(data_atual)

    context = {
        "perfil": perfil,
        "aniversariantes": aniversariantes_list,
        "usuarios": usuarios,
        "postagens": postagens,
        "user_likes": user_likes,
        "cidade": cidade,
        "temp": temp,
        "estacao": estacao,
    }
    return render(request, "dashboard/home.html", context)
