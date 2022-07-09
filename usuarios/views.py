from django.shortcuts import render
from visitantes.models import Visitante


def index(request):

    todos_visitantes = Visitante.objects.all()

    contex = {
            "name_pagina": "Início da Dashboard",
            "todos_visitantes": todos_visitantes,
    }

    return render(request, 'index.html', contex)


