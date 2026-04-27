from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projetos/editar/<int:id>/', views.edita_projeto_view, name='edita_projeto'),
    path('projetos/apagar/<int:id>/', views.apaga_projeto_view, name='apaga_projeto'),
    path('tecnologia/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/editar/<int:id>/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologias/apagar/<int:id>/', views.apaga_tecnologia_view, name='apaga_tecnologia'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencias/editar/<int:id>/', views.edita_competencia_view, name='edita_competencia'),
    path('competencias/apagar/<int:id>/', views.apaga_competencia_view, name='apaga_competencia'),
    path('makingof/', views.makingof_view, name='makingof'),
]