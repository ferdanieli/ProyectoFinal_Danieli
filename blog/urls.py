from django.urls import path
from blog.views import show_html, CrearCarrera, DetalleCarrera, CarreraList

urlpatterns = [
    path('crear/', CrearCarrera.as_view()),
    path('carreras/', CarreraList.as_view(), name= "CarreraList"),
    path('carrera/<int:pk>', DetalleCarrera.as_view(), name="CarreraDetail"),
    path('show/', show_html),
]
