from django.shortcuts import render, redirect
from usuario.models import Perfil
# from .models import Post, Like, Comment
# from .forms import CommentForm
from random import shuffle
from django.db.models import Q
from .models import Post, Comentarios
from .forms import PostForm,ComentarioForm

def social(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    usuarios = Perfil.objects.all()
    usuarios_list = list(usuarios)
    shuffle(usuarios_list)
    postagens = Post.objects.order_by('-criado_em').prefetch_related('comentarios_set')
    comentarios = Comentarios.objects.order_by('-criado_em')
    context = {
        "perfil":perfil,
        "usuarios": usuarios,
        "postagens": postagens,
        "comentarios": comentarios,
    }
    
    if request.method == 'GET':
        return render(request, 'social/social.html', context)
    
    elif request.method == "POST" and 'form_post' in request.POST:
        form_post = PostForm(request.POST, request.FILES)
        context = {
        "form_post": form_post,
        }
        if form_post.is_valid():
            form_post.save()
            form_post = PostForm()
            return redirect('social')
        else:
            return redirect('social')
    
    elif request.method == "POST" and 'form_comentario' in request.POST:
        form_comentario = ComentarioForm(request.POST, request.FILES)
        context = {
            "form_comentario":form_comentario,
        }
        if form_comentario.is_valid():
            form_comentario.save()
            form_comentario = ComentarioForm()
            return redirect('social')
        else:
            return redirect('social')
        

def editPost(request, post_edit_id):
    post = Post.objects.get(id=post_edit_id)
    form_post = PostForm(request.POST, request.FILES, instance=post)
    if form_post.is_valid():
        form_post.save()
        return redirect('social')
    return redirect('social')
        
def excluir_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('social')
        
def excluir_comentario(request, post_id):
    comentario = Comentarios.objects.get(id=post_id)
    comentario.delete()
    return redirect('social')


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

