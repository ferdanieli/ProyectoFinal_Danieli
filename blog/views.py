from django.shortcuts import render
from blog.models import Carrera


def show_html(request):
    carrera = Carrera.objects.first()
    contexto = {"carrera": carrera}
    return render(request, 'index.html', contexto)
