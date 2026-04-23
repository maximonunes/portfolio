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
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('cursos/', views.cursos_view, name='cursos'),
]