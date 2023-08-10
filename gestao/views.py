from django.shortcuts import render
from .models import Qualidade
from pathlib import Path 

def qualidade(request):
    docs_qualidade = Qualidade.objects.order_by('-modificado')
    lista =[]
    for i in docs_qualidade:
        sz = Path(f'media/{i.doc.name}').stat().st_size
        lista.append(sz)
    lista_completa = zip(docs_qualidade, lista)
    return render(request, 'gestao/qualidade.html', {"docs": lista_completa})
