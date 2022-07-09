from django.shortcuts import render

def registrar_visitante(request):

    contex = {

    }

    return render(request, "registrar_visitante.html", contex)

