from django.urls import path
from .views import documentos, qualidade, comercial, controladoria, departamento_pessoal,\
engenharia, financeiro,fiscal, juridico, logistica, marketing, meio_ambiente, orcamentos, pmo,\
recursos_humanos, seguranca_do_trabalho, sistemas, suprimentos, ti, vendas

urlpatterns = [
    path("", documentos , name='documentos'),
    path("comercial/", comercial, name='documentos/comercial'),
    path("controladoria/", controladoria, name='documentos/controladoria'),
    path("departamento_pessoal/", departamento_pessoal, name='documentos/departamento_pessoal'),
    path("engenharia/", engenharia, name='documentos/engenharia'),
    path("financeiro/", financeiro, name='documentos/financeiro'),
    path("fiscal/", fiscal, name='documentos/fiscal'),
    path("juridico/", juridico, name='documentos/juridico'),
    path("logistica/", logistica, name='documentos/logistica'),
    path("marketing/", marketing, name='documentos/marketing'),
    path("meio_ambiente/", meio_ambiente, name='documentos/meio_ambiente'),
    path("orcamentos/", orcamentos, name='documentos/orcamentos'),
    path("pmo/", pmo, name='documentos/pmo'),
    path("qualidade/", qualidade, name='documentos/qualidade'),
    path("recursos_humanos/", recursos_humanos, name='documentos/recursos_humanos'),
    path("seguranca_do_trabalho/", seguranca_do_trabalho, name='documentos/seguranca_do_trabalho'),
    path("sistemas/", sistemas, name='documentos/sistemas'),
    path("suprimentos/", suprimentos, name='documentos/suprimentos'),
    path("ti/", ti, name='documentos/ti'),
    path("vendas/", vendas, name='documentos/vendas'),
]