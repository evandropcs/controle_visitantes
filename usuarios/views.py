from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    contex = {
            "name_pagina": "Início da Dashboard",
    }

    return render(request, 'index.html', contex)


