from datetime import date, datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import redirect, render

from calendario.models import Events
from usuario.models import Perfil

TIME_ZONE = "UTC"


def calendario(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id_usuario = int(request.user.id)
    perfil = Perfil.objects.get(usuario_id=id_usuario)
    all_events = Events.objects.filter(user=id_usuario)

    context = {
        "perfil": perfil,
        "id_usuario": id_usuario,
        "events": all_events,
    }

    return render(request, "calendario/calendario.html", context)


def all_events(request):
    id_usuario = request.user.id
    all_events = Events.objects.filter(user=id_usuario)
    aniversarios = Perfil.objects.all()
    publicos = Events.objects.filter(public=True)
    data_atual = date.today()
    ano_atual = data_atual.year

    out = []

    for publico in publicos:
        if publico.user.id != id_usuario:
            out.append(
                {
                    "title": publico.name,
                    "start": publico.start.strftime("%Y-%m-%d %H:%M"),
                    "end": publico.end.strftime("%Y-%m-%d %H:%M"),
                    "allDay": publico.allDay,
                }
            )

    for aniversario in aniversarios:
        data_aniversario = aniversario.nascimento
        if data_aniversario is not None:
            out.append(
                {
                    "title": f"Aniversariante {aniversario.nome} {aniversario.sobrenome}",
                    "start": f"{ano_atual}-{aniversario.nascimento.month:02d}-{aniversario.nascimento.day:02d}",
                    "allDay": True,
                }
            )

    for aniversario in aniversarios:
        # Adiciona 1 ao ano atual para marcar o aniversário no próximo ano
        ano_aniversario = ano_atual + 1
        data_aniversario = aniversario.nascimento
        if data_aniversario is not None:
            out.append(
                {
                    "title": f"Aniversariante {aniversario.nome} {aniversario.sobrenome}",
                    "start": f"{ano_aniversario}-{aniversario.nascimento.month:02d}-{aniversario.nascimento.day:02d}",
                    "allDay": True,
                }
            )

    for event in all_events:
        start = event.start - timedelta(hours=3)
        end = event.end - timedelta(hours=3)
        out.append(
            {
                "title": event.name,
                "user": event.user_id,
                "id": event.id,
                "start": start.strftime("%Y-%m-%d %H:%M"),
                "end": end.strftime("%Y-%m-%d %H:%M"),
                "allDay": event.allDay,
            }
        )

    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    user = request.GET.get("user", None)

    try:
        if "T" in start and "Z" in start:
            start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
        else:
            start = datetime.strptime(start, "%Y-%m-%d")

        if "T" in end and "Z" in end:
            end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")
        else:
            end = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        # Tratamento de exceção se as strings de data não estiverem no formato esperado
        data = {"error": "Formato de data inválido."}
        return JsonResponse(data, status=400)

    # Verificando se a diferença entre as datas é maior que 12 horas
    if (end - start) > timedelta(hours=12):
        allDay = True
    else:
        allDay = False

    # Criando e salvando o evento
    event = Events(
        name=str(title),
        start=start,
        end=end,
        user_id=int(user),
        allDay=allDay,
    )
    event.save()

    data = {"success": "Evento adicionado com sucesso."}
    return JsonResponse(data)


def update(request):
    start_inicio = request.GET.get("start", None)

    data_start = datetime.fromisoformat(start_inicio[:-1])

    data_3 = data_start + timedelta(hours=3)

    start = data_3.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    end_inicio = request.GET.get("end", None)

    data_end = datetime.fromisoformat(end_inicio[:-1])

    data_end_3 = data_end + timedelta(hours=3)

    end = data_end_3.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    user = request.GET.get("user", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.user_id = user
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
