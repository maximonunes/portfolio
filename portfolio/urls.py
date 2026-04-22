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
]