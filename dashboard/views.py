from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from usuario.models import Perfil
from django.utils import timezone
from random import shuffle
from django.db.models import Prefetch
from social.models import Post, Comentarios, Like
from social.forms import PostForm, ComentarioForm


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)

    mes_atual = timezone.now().month
    aniversariantes = Perfil.objects.filter(nascimento__month=mes_atual)

    aniversariantes_list = list(aniversariantes)
    shuffle(aniversariantes_list)

    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    postagens = Post.objects.order_by("-criado_em").prefetch_related(
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
    }
    print(perfil)
    return render(request, "dashboard/home.html", context)
