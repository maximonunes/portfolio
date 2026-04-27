from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto  # Confirma se o teu modelo se chama Projeto
from .forms import ProjetoForm
from .forms import TecnologiaForm
from .forms import FormacaoForm
from .forms import CompetenciaForm
from .models import Tecnologia, UnidadeCurricular, TFC , Curso, Formacao, Competencia


# Página Inicial do Portfólio
def home_view(request):
    return render(request, 'portfolio/home.html')


def sobre_view(request):
    return render(request , 'portfolio/sobre.html')

# Listar Projetos
def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

# Criar Novo Projeto
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Adicionar Projeto'})

# Editar Projeto Existente
def edita_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Editar Projeto'})

# Apagar Projeto
def apaga_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'item': projeto})


# View para adicionar tecnologia
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home') # Redireciona para onde quiseres
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Nova Tecnologia'})


# Tudo daqui para baixo foi adicionado com base na ficha 7
def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {
        'tecnologias': tecnologias
    })


def edita_tecnologia_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Editar Tecnologia'})


def apaga_tecnologia_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'item': tecnologia})
def ucs_view(request):
    ucs = UnidadeCurricular.objects.all()
    return render(request, 'portfolio/ucs.html', {
        'ucs': ucs
    })

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {
        'tfcs': tfcs
    })

def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'portfolio/cursos.html', {
        'cursos': cursos
    })

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Nova Formação'})


def edita_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/formulario.html', {'form': form, 'titulo': 'Editar Formação'})


def apaga_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'item': formacao})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {
        'competencias': competencias
    })

# CRIAR
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/formulario.html', {
        'form': form,
        'titulo': 'Nova Competência'
    })

# EDITAR
def edita_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/formulario.html', {
        'form': form,
        'titulo': 'Editar Competência'
    })

# APAGAR
def apaga_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'item': competencia
    })

def makingof_view(request):
    registos = MakingOf.objects.all().order_by('-data')
    return render(request, 'portfolio/makingof.html', {
        'registos': registos
    })