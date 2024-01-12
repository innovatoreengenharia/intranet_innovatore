from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Perfil
from .models import Noticia, Bloco, Comunicado, Quadro
from .forms import BlocoForm, ComunicadoForm, QuadroForm, NoticiaForm
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from django.db.models import Q
import json
from django.core.paginator import Paginator


def informativos(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    noticias = Noticia.objects.filter(destaque=False).order_by("-publicado_em")[:4]
    noticias_em_destaque = Noticia.objects.filter(destaque=True).order_by(
        "-publicado_em"
    )
    comunicados = Comunicado.objects.order_by("-publicado_em")[:3]
    quadros = Quadro.objects.order_by("-publicado_em")[:4]

    if quadros:
        # Separando o último quadro em uma variável
        ultimo_quadro = quadros[0]

        # Separando os outros três quadros em outra variável
        outros_quadros = quadros[1:]
    else:
        # Caso não haja nenhum quadro na lista
        ultimo_quadro = None
        outros_quadros = []

    context = {
        "perfil": perfil,
        "id_usuario": id_usuario,
        "noticias_em_destaque": noticias_em_destaque,
        "noticias": noticias,
        "comunicados": comunicados,
        "ultimo_quadro": ultimo_quadro,
        "outros_quadros": outros_quadros,
    }

    return render(request, "informativos/informativos.html", context)


def noticia(request, id):
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    noticia = get_object_or_404(Noticia, pk=id)

    blocos = Bloco.objects.filter(noticia_id=noticia.id)

    # Obtém as tags da notícia atual
    tags_do_objeto = noticia.obter_lista_de_tags()

    # Inicializa a lista de notícias relacionadas
    tags_relacionadas = []

    # Se a notícia atual possui tags, busca notícias relacionadas
    if tags_do_objeto:
        # Filtra notícias que têm tags em comum com a notícia atual
        for tag in tags_do_objeto:
            # Adiciona resultados à lista apenas se ainda não estiverem presentes
            tags_relacionadas += (
                Noticia.objects.filter(Q(tags__icontains=tag) | Q(tags__iexact=tag))
                .exclude(pk=id)
                .exclude(pk__in=[n.pk for n in tags_relacionadas])
            )[:3]

    # Prepara o contexto
    context = {
        "perfil": perfil,
        "noticia": noticia,
        "tags_do_objeto": tags_do_objeto,
        "tags_relacionadas": tags_relacionadas,
        "blocos": blocos,
    }

    return render(request, "informativos/noticia.html", context)


def criar_noticia(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    noticia_form = Noticia()

    form_bloco_factory = inlineformset_factory(Noticia, Bloco, BlocoForm, extra=1)
    form_bloco = form_bloco_factory(instance=noticia_form)

    context = {
        "perfil": perfil,
        "id_usuario": id_usuario,
        "form_bloco": form_bloco,
    }

    return render(request, "informativos/criar_noticia.html", context)


def convert_image(b64: str, name: str) -> ContentFile:
    format, imgstr = b64.split(";base64,")
    # ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=name)


@csrf_exempt
def add_noticia(request):
    # Pega o que vem da requisição
    titulo = request.POST.get("titulo", None)
    paragrafo = request.POST.get("paragrafo", None)
    tags = request.POST.get("tags", None)

    imagem_b64 = request.POST.get("imagem", None)
    imagem_destaque_b64 = request.POST.get("imagem_destaque", None)
    imagem_thumb_b64 = request.POST.get("imagem_thumb", None)
    imagem_noticia_b64 = request.POST.get("imagem_noticia", None)

    nome_imagem = request.POST.get("nome_imagem", None)
    nome_imagem_destaque = request.POST.get("nome_imagem_destaque", None)
    nome_imagem_thumb = request.POST.get("nome_imagem_thumb", None)
    nome_imagem_noticia = request.POST.get("nome_imagem_noticia", None)
    destaque = request.POST.get("destaque_checkbox", None)

    # Transformar as imagens de base64 para ContentFile
    imagem = convert_image(imagem_b64, nome_imagem)
    imagem_destaque = convert_image(imagem_destaque_b64, nome_imagem_destaque)
    imagem_thumb = convert_image(imagem_thumb_b64, nome_imagem_thumb)
    imagem_noticia = convert_image(imagem_noticia_b64, nome_imagem_noticia)

    # Instanciar objeto Noticia e salvar
    noticia = Noticia(
        titulo=titulo,
        imagem=imagem,
        tags=tags,
        imagem_destaque=imagem_destaque,
        imagem_thumb=imagem_thumb,
        imagem_noticia=imagem_noticia,
        destaque=destaque,
        paragrafo=paragrafo,
    )

    noticia.save()

    blocos_json = request.POST.get("blocos", None)
    blocos = json.loads(blocos_json)
    for bloco in blocos:
        titulo_bloco = bloco["titulo_bloco"]
        paragrafo_bloco = bloco["paragrafo_bloco"]

        if bloco.get("imagem_bloco"):
            imagem_bloco = convert_image(
                bloco["imagem_bloco"], bloco["nome_imagem_bloco"]
            )
            bloco_save = Bloco(
                noticia=noticia,
                imagem_bloco=imagem_bloco,
                titulo_bloco=titulo_bloco,
                paragrafo_bloco=paragrafo_bloco,
            )
        else:
            bloco_save = Bloco(
                noticia=noticia,
                titulo_bloco=titulo_bloco,
                paragrafo_bloco=paragrafo_bloco,
            )
        bloco_save.save()

    return JsonResponse(
        data={},
    )


def todas_noticias(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    noticias = Noticia.objects.order_by("-publicado_em")

    buscar_filtro = request.GET.get("buscar")
    if buscar_filtro:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=buscar_filtro)
            | Q(paragrafo__icontains=buscar_filtro)
            | Q(tags__icontains=buscar_filtro)
        )
    documento_paginator = Paginator(noticias, 100)
    page_num = request.GET.get("page")
    page = documento_paginator.get_page(page_num)

    context = {
        "perfil": perfil,
        "noticias": page.object_list,
        "page": page,
    }
    return render(request, "informativos/todas_noticias.html", context)


def editar_noticia(request, id_noticia):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)
        noticia = Noticia.objects.get(id=id_noticia)

        form = NoticiaForm(instance=noticia)

        form_bloco_factory = inlineformset_factory(
            Noticia, Bloco, form=BlocoForm, extra=1
        )
        form_bloco = form_bloco_factory(instance=noticia)

        context = {
            "perfil": perfil,
            "form": form,
            "form_bloco": form_bloco,
        }
        return render(request, "informativos/editar_noticia.html", context)

    elif request.method == "POST":
        usuario_id = request.user.id
        noticia = Noticia.objects.get(id=id_noticia)

        form = NoticiaForm(request.POST, request.FILES, instance=noticia)

        form_bloco_factory = inlineformset_factory(Noticia, Bloco, form=BlocoForm)
        form_bloco = form_bloco_factory(request.POST, request.FILES, instance=noticia)

        if form.is_valid() and form_bloco.is_valid():
            principal = form.save()
            form_bloco.instance = principal
            form_bloco.save()
            return redirect("informativos")
        else:
            context = {
                "usuario_id": usuario_id,
                "perfil": perfil,
                "form": form,
                "form_bloco": form_bloco,
            }
            return render(request, "informativos/editar_noticia.html", context)


def deletar_noticia(request, id):
    noticia = Noticia.objects.get(pk=id)
    noticia.delete()
    return redirect("informativos")


def criar_comunicado(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "GET":
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)

        context = {
            "perfil": perfil,
        }
        return render(request, "informativos/criar_comunicado.html", context)

    elif request.method == "POST":
        form = ComunicadoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse("informativos"))

        else:
            context = {
                "form": form,
            }


def editar_comunicado(request, id_comunicado):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        comunicado = Comunicado.objects.get(id=id_comunicado)
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)

        form = ComunicadoForm(instance=comunicado)

        context = {
            "perfil": perfil,
            "form": form,
        }
        return render(request, "informativos/editar_comunicado.html", context)
    elif request.method == "POST":
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)
        comunicado = Comunicado.objects.get(id=id_comunicado)
        form = ComunicadoForm(request.POST, instance=comunicado)

        if form.is_valid():
            form.save()
            return redirect("informativos")
        else:
            return redirect("informativos")


def todos_comunicados(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    comunicados = Comunicado.objects.order_by("-publicado_em")
    buscar_filtro = request.GET.get("buscar")
    if buscar_filtro:
        comunicados = Comunicado.objects.filter(
            Q(titulo__icontains=buscar_filtro) | Q(paragrafo__icontains=buscar_filtro)
        )

    documento_paginator = Paginator(comunicados, 100)
    page_num = request.GET.get("page")
    page = documento_paginator.get_page(page_num)

    context = {
        "perfil": perfil,
        "comunicados": page.object_list,
        "page": page,
    }
    return render(request, "informativos/todos_comunicados.html", context)


def deletar_comunicado(request, id):
    comunicado = Comunicado.objects.get(pk=id)
    comunicado.delete()
    return redirect("informativos")


def criar_quadro(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)

        context = {
            "perfil": perfil,
        }
        return render(request, "informativos/criar_quadro.html", context)

    elif request.method == "POST":
        form = QuadroForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse("informativos"))

        else:
            context = {
                "form": form,
            }


def editar_quadro(request, id_quadro):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        quadro = Quadro.objects.get(id=id_quadro)
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)

        form = QuadroForm(instance=quadro)

        context = {
            "perfil": perfil,
            "form": form,
        }
        return render(request, "informativos/editar_quadro.html", context)

    elif request.method == "POST":
        id_usuario = int(request.user.id)
        perfil = Perfil.objects.get(usuario_id=id_usuario)
        quadro = Quadro.objects.get(id=id_quadro)
        form = QuadroForm(request.POST, instance=quadro)

        if form.is_valid():
            form.save()
            return redirect("informativos")
        else:
            return redirect("informativos")


def todos_quadros(request):
    if not request.user.is_authenticated:
        return redirect("login")
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    quadros = Quadro.objects.order_by("-publicado_em")
    buscar_filtro = request.GET.get("buscar")
    if buscar_filtro:
        quadros = Quadro.objects.filter(
            Q(titulo__icontains=buscar_filtro) | Q(paragrafo__icontains=buscar_filtro)
        )

    documento_paginator = Paginator(quadros, 100)
    page_num = request.GET.get("page")
    page = documento_paginator.get_page(page_num)

    context = {
        "perfil": perfil,
        "quadros": page.object_list,
        "page": page,
    }
    return render(request, "informativos/todos_quadros.html", context)


def deletar_quadro(request, id):
    quadro = Quadro.objects.get(pk=id)
    quadro.delete()
    return redirect("informativos")


def quadro(request, id_quadro):
    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    quadro = get_object_or_404(Quadro, pk=id_quadro)

    context = {
        "perfil": perfil,
        "quadro": quadro,
    }

    return render(request, "informativos/quadro.html", context)
