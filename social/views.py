from django.shortcuts import render, redirect
from usuario.models import Perfil
from datetime import date
from usuario.models import Perfil, Experiencia, Formacao, Cursos, Habilidades, Hobbies
# from .models import Post, Like, Comment
# from .forms import CommentForm
from random import shuffle
from django.db.models import Q

def social(request):

    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    # post = Post.objects.all()

    context = {
        "perfil":perfil,
        "usuarios": usuarios,
    }
    return render(request, 'social/social.html', context)

# def like_post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     Like.objects.create(user=request.user, post=post)
#     return redirect('social/social.html')

# def add_comment(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('social/social.html')
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment.html', {'form': form})


def contatos(request):

    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)

    buscar_filtro = request.GET.get('buscar')
    if buscar_filtro:
        usuarios_list = Perfil.objects.filter(
                                            Q (nome__icontains=buscar_filtro) |
                                            Q(sobrenome__icontains=buscar_filtro) |  
                                            Q(obra_trabalho__icontains=buscar_filtro) 
                                              )

    context = {
        "perfil":perfil,
        "usuarios": usuarios_list,
    }

    return render(request, 'social/contatos.html', context)

