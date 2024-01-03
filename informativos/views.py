from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Perfil
from .models import Noticia, Bloco
from .forms import NoticiaForm, BlocoForm, ComunicadoForm
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from django.db.models import Q
import json


def informativos(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    noticias = Noticia.objects.filter(destaque=False).order_by("-publicado_em")[:4]
    noticias_em_destaque = Noticia.objects.filter(destaque=True).order_by(
        "-publicado_em"
    )

    context = {
        "perfil": perfil,
        "id_usuario": id_usuario,
        "noticias_em_destaque": noticias_em_destaque,
        "noticias": noticias,
    }

    return render(request, "informativos/informativos.html", context)


def noticia(request, id):
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

    """ form_bloco_factory = inlineformset_factory(Noticia, Bloco, BlocoForm)
    form_bloco = form_bloco_factory(request.POST, instance=noticia)
    form_bloco.save() """

    blocos_json = request.POST.get("blocos", None)
    blocos = json.loads(blocos_json)
    for bloco in blocos:
        titulo_boco = bloco["titulo_bloco"]
        paragrafo_bloco = bloco["paragrafo_bloco"]
        bloco_save = Bloco(
            noticia=noticia,
            titulo_bloco=titulo_boco,
            paragrafo_bloco=paragrafo_bloco,
        )
        bloco_save.save()

    return JsonResponse(
        data={},
    )


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
            print("ERRO NO CADASTRO", form.errors, usuario_id)
            return render(request, "usuario/form.html", context)
