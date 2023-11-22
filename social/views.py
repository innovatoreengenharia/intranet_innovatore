from django.shortcuts import render, redirect
from usuario.models import Perfil

# from .models import Post, Like, Comment
# from .forms import CommentForm
from random import shuffle
from django.db.models import Q
from .models import Post, Comentarios, Like
from .forms import PostForm, ComentarioForm
from django.db.models import Prefetch


def social(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    postagens = Post.objects.order_by("-criado_em").prefetch_related(
        Prefetch("comentarios_set", queryset=Comentarios.objects.order_by("criado_em")),
        Prefetch("like_set", queryset=Like.objects.all()),
    )
    user_likes = [item.post.id for item in Like.objects.filter(user=perfil)]

    context = {
        "perfil": perfil,
        "usuarios": usuarios,
        "postagens": postagens,
        "user_likes": user_likes,
    }

    if request.method == "GET":
        return render(request, "social/social.html", context)

    elif request.method == "POST" and "form_post" in request.POST:
        form_post = PostForm(request.POST, request.FILES)
        context = {
            "form_post": form_post,
        }
        if form_post.is_valid():
            form_post.save()
            form_post = PostForm()
            return redirect("social")
        else:
            return redirect("social")

    elif request.method == "POST" and "form_comentario" in request.POST:
        form_comentario = ComentarioForm(request.POST, request.FILES)
        context = {
            "form_comentario": form_comentario,
        }
        if form_comentario.is_valid():
            form_comentario.save()
            form_comentario = ComentarioForm()
            return redirect("social")
        else:
            return redirect("social")


def editPost(request, post_edit_id):
    post = Post.objects.get(id=post_edit_id)
    form_post = PostForm(request.POST, request.FILES, instance=post)
    if form_post.is_valid():
        form_post.save()
        return redirect("social")
    return redirect("social")


def excluir_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("social")


def editComentario(request, comentario_edit_id):
    comentario = Comentarios.objects.get(id=comentario_edit_id)
    form_comentario = ComentarioForm(request.POST, instance=comentario)
    if form_comentario.is_valid():
        form_comentario.save()
        return redirect("social")
    return redirect("social")


def excluir_comentario(request, post_id):
    comentario = Comentarios.objects.get(id=post_id)
    comentario.delete()
    return redirect("social")


def contatos(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)

    buscar_filtro = request.GET.get("buscar")
    if buscar_filtro:
        usuarios_list = Perfil.objects.filter(
            Q(nome__icontains=buscar_filtro)
            | Q(sobrenome__icontains=buscar_filtro)
            | Q(obra_trabalho__icontains=buscar_filtro)
        )

    context = {
        "perfil": perfil,
        "usuarios": usuarios_list,
    }

    return render(request, "social/contatos.html", context)
