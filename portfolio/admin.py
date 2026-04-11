from django.contrib import admin
from .models import (
    Curso, UnidadeCurricular, TFC, Tecnologia, 
    Projeto, Formacao, Competencia, MakingOf, 
    Perfil, Docente, Interesse
)

# Registo direto de todas as entidades
admin.site.register(Curso)
admin.site.register(UnidadeCurricular)
admin.site.register(TFC)
admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(Formacao)
admin.site.register(Competencia)
admin.site.register(MakingOf)
admin.site.register(Perfil)
admin.site.register(Docente)
admin.site.register(Interesse)