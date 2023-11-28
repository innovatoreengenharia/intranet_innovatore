from django.shortcuts import render, redirect
from usuario.models import Perfil
from django.http import JsonResponse
from calendario.models import Events


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

    out = []
    for event in all_events:
        out.append(
            {
                "title": event.name,
                "user": event.user_id,
                "id": event.id,
                "start": event.start.strftime("%Y-%m-%d"),
                "end": event.end.strftime("%Y-%m-%d"),
            }
        )
    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    user = request.GET.get("user", None)
    event = Events(name=str(title), start=start, end=end, user_id=int(user))
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    user = request.GET.get("user", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.user = user
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
