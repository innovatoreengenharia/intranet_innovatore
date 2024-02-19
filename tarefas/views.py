from django.shortcuts import render, redirect
from usuario.models import Perfil
from tarefas.models import Quadros, Colunas, Tarefas
from tarefas.forms import QuadroForm

def tarefas(request):
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    usuarios = Perfil.objects.all()
    quadros_usuario = Quadros.objects.filter(usuario = perfil)
    context = {
        "perfil": perfil,
        "usuarios": usuarios,
        "quadros_usuario": quadros_usuario,
    }
    if request.method == "GET":
        return render(request, 'tarefas/tarefas.html', context)
    
    elif request.method == "POST" and "criar_quadro" in request.POST:
        form = QuadroForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")
    
def quadro(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id = id_usuario)
    usuarios = Perfil.objects.all()
    #  Quadros que cada usuario possui
    quadros_usuario = Quadros.objects.filter(usuario = perfil)
    context = {
        "perfil": perfil,
        "quadro": quadro,
        "usuarios": usuarios,
        "quadros_usuario": quadros_usuario,
    }
    if request.method == "GET":
        return render(request, 'tarefas/quadro.html', context)

    elif request.method == "POST" and "criar_quadro" in request.POST:
        form = QuadroForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")
    
    elif request.method == "POST" and "add_usuario" in request.POST:
        form = QuadroForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")
    

def adicionar_participante(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)

    if request.method == "POST":
        usuario_id = request.POST.get('usuario')
        usuario = Perfil.objects.get(id=usuario_id)

        # Adicione o usuário selecionado ao quadro existente
        quadro.usuario.add(usuario)
        quadro.save()

        return redirect("quadro", id_quadro)  # Redirecionar para uma página de sucesso após adicionar o usuário ao quadro

    return redirect("quadro", id_quadro)

def remover_participante(request, id_quadro, id_usuario):
    quadro = Quadros.objects.get(id=id_quadro)
    usuario = Perfil.objects.get(id=id_usuario)

    # Remova o usuário do quadro
    quadro.usuario.remove(usuario)
    quadro.save()

    return redirect("quadro", id_quadro)

def alterar_titulo_quadro(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)

    if request.method == "POST":
        novo_titulo = request.POST.get('novo_titulo')

        # Alterar o título do quadro para o novo título fornecido
        quadro.titulo = novo_titulo
        quadro.save()

        return redirect("quadro", id_quadro)  # Redirecionar para uma página de sucesso após alterar o título do quadro

    return redirect("quadro", id_quadro)