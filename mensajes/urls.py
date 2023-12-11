from django.urls import path

from blog.views import show_html
from mensajes.views import comentario

urlpatterns = [
    path('comentarios/', comentario),
    path('show/', show_html),
]
