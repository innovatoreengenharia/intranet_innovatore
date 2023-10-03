from django.shortcuts import render,redirect
from usuario.models import Perfil
from .models import Comercial, Controladoria, DepartamentoPessoal, Engenharia, Financeiro, Fiscal, Juridico, Logistica, Marketing, MeioAmbiente,Orcamentos, PMO, Qualidade, RecursosHumanos, SegurancaDoTrabalho, Sistemas, Suprimentos, TI, Vendas
from pathlib import Path 
from django.core.paginator import Paginator

def documentos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()
    context = {
        'perfil': perfil,
    }
    return render(request, 'documentos/documentos.html', context)

    

def buscar(request, modelo, nome, busca):
    if not request.user.is_authenticated:
        return redirect('login')
    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()

    documentos = modelo.objects.order_by('-modificado')
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            doc_encontrado = documentos.filter(nome__icontains=nome_a_buscar)
            lista = []
            for i in doc_encontrado:
                sz = Path(f'media/{i.doc.name}').stat().st_size
                lista.append(sz)
            lista_completa = zip(doc_encontrado, lista)
    context = {
        "nome":nome,
        "lista_completa": lista_completa,
        "perfil": perfil,
        "busca": busca,
    }
    return context

def render_model(request, modelo, url, nome, busca):
    if not request.user.is_authenticated:
        return redirect('login')

    id_usuario = request.user.id
    perfil = Perfil.objects.filter(usuario_id = id_usuario).first()
    docs_modelo = modelo.objects.order_by('-modificado')

    documento_paginator = Paginator(docs_modelo, 10)
    page_num = request.GET.get('page')
    page = documento_paginator.get_page(page_num)

    lista = []
    for i in page:
        sz = Path(f'media/{i.doc.name}').stat().st_size
        lista.append(sz)
    lista_completa = zip(page, lista)
    context = {
        "nome":nome,
        "page": page,
        "lista_completa": lista_completa,
        "perfil":perfil,
        "url":url,
        "busca":busca,
    } 
    return context
    

def comercial(request):
    return render(request, 'documentos/doc.html',render_model(request, Comercial, 'documentos/comercial', 'Comercial', 'buscarComercial/') )
def buscarComercial(request):
    return render(request, 'documentos/doc.html',buscar(request, Comercial, 'Comercial','buscarComercial/') )

def controladoria(request):
    return render(request, 'documentos/doc.html',render_model(request, Controladoria, 'documentos/controladoria', 'Controladoria', 'buscarControladoria/') )
def buscarControladoria(request):
    return render(request, 'documentos/doc.html',buscar(request, Controladoria) )

def departamento_pessoal(request):
    return render(request, 'documentos/doc.html',render_model(request, DepartamentoPessoal, 'documentos/departamento_pessoal', 'Departamento Pessoal') )

def engenharia(request):
    return render(request, 'documentos/doc.html',render_model(request, Engenharia, 'documentos/engenharia', 'Engenharia') )

def financeiro(request):
    return render(request, 'documentos/doc.html',render_model(request, Financeiro, 'documentos/financeiro', 'Financeiro') )

def fiscal(request):
    return render(request, 'documentos/doc.html',render_model(request, Fiscal, 'documentos/fiscal', 'Fiscal') )

def juridico(request):
    return render(request, 'documentos/doc.html',render_model(request, Juridico, 'documentos/juridico', 'Jurídico') )

def logistica(request):
    return render(request, 'documentos/doc.html',render_model(request, Logistica, 'documentos/logistica', 'Logística') )

def marketing(request):
    return render(request, 'documentos/doc.html',render_model(request, Marketing, 'documentos/marketing', 'Marketing') )

def meio_ambiente(request):
    return render(request, 'documentos/doc.html',render_model(request, MeioAmbiente, 'documentos/meio_ambiente', 'Meio Ambiente') )

def orcamentos(request):
    return render(request, 'documentos/doc.html',render_model(request, Orcamentos, 'documentos/orcamentos', 'Orçamentos') )

def pmo(request):
    return render(request, 'documentos/doc.html',render_model(request, PMO, 'documentos/pmo', 'P.M.O.') )

def qualidade(request):
    return render(request, 'documentos/doc.html', render_model(request, Qualidade, 'documentos/qualidade', 'Qualidade'))

def recursos_humanos(request):
    return render(request, 'documentos/doc.html',render_model(request, RecursosHumanos, 'documentos/recursos_humanos', 'Recursos Humanos') )

def seguranca_do_trabalho(request):
    return render(request, 'documentos/doc.html',render_model(request, SegurancaDoTrabalho, 'documentos/seguranca_do_trabalho', 'Seguraça do Trabalho') )

def sistemas(request):
    return render(request, 'documentos/doc.html',render_model(request, Sistemas, 'documentos/sistemas', 'Sistemas') )

def suprimentos(request):
    return render(request, 'documentos/doc.html',render_model(request, Suprimentos, 'documentos/suprimentos', 'Suprimentos') )

def ti(request):
    return render(request, 'documentos/doc.html',render_model(request, TI, 'documentos/ti', 'T.I.') )

def vendas(request):
    return render(request, 'documentos/doc.html',render_model(request, Vendas, 'documentos/vendas', 'Vendas') )



