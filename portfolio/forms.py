from django import forms
from .models import Projeto, Tecnologia # Certifica-te que importas ambos

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TecnologiaForm(forms.ModelForm): # Esta classe tem de existir!
    class Meta:
        model = Tecnologia
        fields = '__all__'