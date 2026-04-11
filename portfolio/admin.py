from django.contrib import admin
# Remove 'Interesse' se não o criaste no models.py, e verifica os outros nomes
from .models import Curso, UnidadeCurricular, TFC, Tecnologia, Projeto, Formacao, Competencia, MakingOf

# Exemplo de registo simples para não dar erro:
admin.site.register(Curso)
admin.site.register(UnidadeCurricular)
admin.site.register(TFC)
admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(Formacao)
admin.site.register(Competencia)
admin.site.register(MakingOf)