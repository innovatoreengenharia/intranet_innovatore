from django.shortcuts import render
from usuario.models import Perfil
from .models import Qualidade
from pathlib import Path 

def documentos(request):
    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()
    context = {
        'perfil': perfil,
    }
    return render(request, 'documentos/documentos.html', context)

def qualidade(request):
    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()
    docs_qualidade = Qualidade.objects.order_by('-modificado')
    lista =[]
    for i in docs_qualidade:
        sz = Path(f'media/{i.doc.name}').stat().st_size
        lista.append(sz)
    lista_completa = zip(docs_qualidade, lista)

    context = {
        "docs": lista_completa,
        'perfil':perfil
    }
    return render(request, 'documentos/qualidade.html', context)

