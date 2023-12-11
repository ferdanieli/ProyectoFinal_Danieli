from django.shortcuts import redirect, render

from blog.models import Carrera
from mensajes.forms import ComentarioForm
from mensajes.models import Comentario


def comentario(request):
    formulario = ComentarioForm(request.POST)

    if formulario.is_valid():
        informacion = formulario.cleaned_data
        carrera = Carrera.objects.get(id= informacion["carrera"])
        comentario_crear = Comentario(usuario= request.user, carrera= carrera, comentario= informacion["comentario"] )

        comentario_crear.save()

        return redirect("/blog/carreras/")

    form = ComentarioForm()
    contexto = {
        "form": form
    }
    return render(request, "mensajes/comentarios.html", contexto)
