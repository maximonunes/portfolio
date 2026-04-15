from django.shortcuts import render
from .models import Curso, Aluno, Professor


def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):
    # Carrega todos os professores e faz prefetch dos cursos que lecionam
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    # Carrega todos os alunos e faz prefetch dos cursos que frequentam
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})
# Create your views here.
