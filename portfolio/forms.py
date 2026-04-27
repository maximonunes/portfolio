from django import forms
from .models import Projeto, Tecnologia, Formacao , Competencia# Certifica-te que importas ambos

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TecnologiaForm(forms.ModelForm): # Esta classe tem de existir!
    class Meta:
        model = Tecnologia
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

from .models import Competencia

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'