from django import forms
from mensajes.models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("usuario", "carrera", "comentario")