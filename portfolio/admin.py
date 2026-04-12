from django.contrib import admin
from .models import (
    Perfil, Docente, Curso, UnidadeCurricular, 
    Tecnologia, TFC, Projeto, Formacao, 
    Competencia, Interesse, MakingOf
)

# 1. PERFIL
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'linkedin', 'github')
    search_fields = ('nome', 'biografia')

admin.site.register(Perfil, PerfilAdmin)

# 2. DOCENTE
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_ciencia_id')
    search_fields = ('nome',)

admin.site.register(Docente, DocenteAdmin)

# 3. CURSO (ou Licenciatura, conforme o teu models.py)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'grau')
    list_display_links = ('nome',)
    search_fields = ('nome', 'codigo')
    list_per_page = 15

admin.site.register(Curso, CursoAdmin)

# 4. UNIDADE CURRICULAR (UC)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_legivel', 'ano', 'semestre', 'ects', 'curso', 'docente_responsavel')
    list_editable = ('ano', 'semestre', 'ects')
    list_filter = ('curso', 'ano', 'semestre')
    search_fields = ('nome', 'codigo_legivel')
    list_per_page = 20

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

# 5. TECNOLOGIA
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    list_editable = ('nivel_interesse',)
    list_filter = ('categoria', 'nivel_interesse')
    search_fields = ('nome', 'acronimo')

admin.site.register(Tecnologia, TecnologiaAdmin)

# 6. PROJETO
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'uc')
    list_filter = ('ano', 'uc', 'tecnologias')
    search_fields = ('titulo', 'descricao')
    filter_horizontal = ('tecnologias',) # Interface de seleção amigável

admin.site.register(Projeto, ProjetoAdmin)

# 7. TRABALHO FINAL DE CURSO (TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano_realizacao', 'curso', 'rating')
    list_editable = ('rating',)
    list_filter = ('curso', 'rating', 'ano_realizacao')
    search_fields = ('titulo', 'autores', 'orientadores')

admin.site.register(TFC, TFCAdmin)

# 8. FORMAÇÃO
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('curso_ou_certificado', 'instituicao', 'data_inicio', 'data_fim')
    list_filter = ('instituicao',)
    date_hierarchy = 'data_inicio'

admin.site.register(Formacao, FormacaoAdmin)

# 9. COMPETÊNCIA
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    list_filter = ('nivel',)
    filter_horizontal = ('projetos',)

admin.site.register(Competencia, CompetenciaAdmin)

# 10. INTERESSE
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icone')

admin.site.register(Interesse, InteresseAdmin)

# 11. MAKING OF
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('etapa', 'data')
    readonly_fields = ('data',)

admin.site.register(MakingOf, MakingOfAdmin)