from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from blog.models import Carrera


class CrearCarrera(CreateView):
    model = Carrera
    success_url = "/blog/carreras/"
    template_name = "blog/crear_carrera.html"
    fields = "__all__"

class CarreraList(ListView):
    model = Carrera
    template_name = "blog/carreras.html"


class DetalleCarrera(DetailView):
    model = Carrera
    template_name = "blog/detalle_carrera.html"

class ActualizacionCarrera(UpdateView):
    model = Carrera
    success_url = "/blog/carreras/"
    template_name = "blog/crear_carrera.html"
    fields = ["descripcion", "imagen"]


class EliminarCarrera(DeleteView):
    model = Carrera
    success_url = "/blog/carreras/"
    template_name = "blog/eliminar_carrera.html"


def show_html(request):
    carrera = Carrera.objects.first()
    contexto = {"carrera": carrera}
    return render(request, 'base.html', contexto)
