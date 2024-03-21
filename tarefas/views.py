from django.shortcuts import redirect, render

from tarefas.forms import ColunaForm, QuadroForm, TarefaForm
from tarefas.models import Colunas, Quadros, Tarefas
from usuario.models import Perfil


def tarefas(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    usuarios = Perfil.objects.all()
    quadros_usuario = Quadros.objects.filter(usuario=perfil)
    context = {
        "perfil": perfil,
        "usuarios": usuarios,
        "quadros_usuario": quadros_usuario,
    }
    if request.method == "GET":
        return render(request, "tarefas/tarefas.html", context)

    elif request.method == "POST" and "criar_quadro" in request.POST:
        form = QuadroForm(request.POST)
        context["form"] = form

        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("tarefas/quadro", id_quadro)

    form = QuadroForm()
    return render(request, "tarefas/tarefas.html", context)


def quadro(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = request.user.id
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    usuarios = Perfil.objects.all()
    #  Quadros que cada usuario possui
    quadros_usuario = Quadros.objects.filter(usuario=perfil)

    colunas = Colunas.objects.filter(quadro=quadro)

    tarefas_por_coluna = {}
    for coluna in colunas:
        tarefas = Tarefas.objects.filter(coluna=coluna)
        tarefas_por_coluna[coluna] = tarefas
        # print(f"Tarefas para {coluna}: {tarefas}")

    context = {
        "perfil": perfil,
        "quadro": quadro,
        "usuarios": usuarios,
        "quadros_usuario": quadros_usuario,
        "colunas": colunas,
        "tarefas_por_coluna": tarefas_por_coluna,
    }
    if request.method == "GET":
        return render(request, "tarefas/quadro.html", context)

    elif request.method == "POST" and "add_usuario" in request.POST:
        form = QuadroForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("tarefas/quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")

    elif request.method == "POST" and "criar_quadro" in request.POST:
        form = QuadroForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            id_quadro = form.instance.id
            return redirect("tarefas/quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")

    elif request.method == "POST" and "criar_coluna" in request.POST:
        form = ColunaForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            return redirect("tarefas/quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")

    elif request.method == "POST" and "criar_tarefa" in request.POST:
        form = TarefaForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            return redirect("tarefas/quadro", id_quadro)
        else:
            form = QuadroForm()
        return redirect("tarefas")


def adicionar_participante(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)

    if request.method == "POST":
        usuario_id = request.POST.get("usuario")
        usuario = Perfil.objects.get(id=usuario_id)

        # Adicione o usuário selecionado ao quadro existente
        quadro.usuario.add(usuario)
        quadro.save()

        return redirect(
            "tarefas/quadro", id_quadro
        )  # Redirecionar para uma página de sucesso após adicionar o usuário ao quadro

    return redirect("tarefas/quadro", id_quadro)


def remover_participante(request, id_quadro, id_usuario):
    quadro = Quadros.objects.get(id=id_quadro)
    usuario = Perfil.objects.get(id=id_usuario)

    # Remova o usuário do quadro
    quadro.usuario.remove(usuario)
    quadro.save()

    return redirect("tarefas/quadro", id_quadro)


def alterar_titulo_quadro(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)

    if request.method == "POST":
        novo_titulo = request.POST.get("novo_titulo")

        # Alterar o título do quadro para o novo título fornecido
        quadro.titulo = novo_titulo
        quadro.save()

        return redirect("tarefas/quadro", id_quadro)

    return redirect("tarefas/quadro", id_quadro)


def remover_quadro(request, id_quadro):
    quadro = Quadros.objects.get(id=id_quadro)
    quadro.delete()

    return redirect("tarefas")


def alterar_titulo_coluna(request, id_quadro, id_coluna):
    coluna = Colunas.objects.get(id=id_coluna)

    if request.method == "POST":
        novo_titulo = request.POST.get("novo_titulo")
        coluna.titulo = novo_titulo
        coluna.save()
        return redirect("tarefas/quadro", id_quadro)

    return redirect("tarefas/quadro", id_quadro)


def alterar_tarefa(request, id_quadro, id_tarefa):
    tarefa = Tarefas.objects.get(id=id_tarefa)

    if request.method == "POST":
        novo_titulo = request.POST.get("novo_titulo")
        tarefa.titulo = novo_titulo
        tarefa.save()
        return redirect("tarefas/quadro", id_quadro)

    return redirect("tarefas/quadro", id_quadro)


def remover_coluna(request, id_quadro, id_coluna):
    coluna = Colunas.objects.get(id=id_coluna)
    coluna.delete()

    return redirect("tarefas/quadro", id_quadro)


def remover_tarefa(request, id_quadro, id_tarefa):
    tarefa = Tarefas.objects.get(id=id_tarefa)
    tarefa.delete()

    return redirect("tarefas/quadro", id_quadro)
