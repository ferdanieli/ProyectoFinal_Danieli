from django.urls import path
from blog.views import show_html, CrearCarrera, DetalleCarrera, CarreraList, ActualizacionCarrera, EliminarCarrera

urlpatterns = [
    path('crear/', CrearCarrera.as_view(), name= "CarreraCreate"),
    path('carreras/', CarreraList.as_view(), name= "CarreraList"),
    path('carrera/<int:pk>', DetalleCarrera.as_view(), name="CarreraDetail"),
    path('editar/<int:pk>', ActualizacionCarrera.as_view(), name="CarreraUpdate"),
    path('eliminar/<int:pk>', EliminarCarrera.as_view(), name="CarreraDelete"),
    path('show/', show_html),
]
