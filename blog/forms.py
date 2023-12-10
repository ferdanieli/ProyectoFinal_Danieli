from django import forms
from blog.models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = "__all__"