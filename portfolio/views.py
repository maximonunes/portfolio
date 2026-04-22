from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto  # Confirma se o teu modelo se chama Projeto
from .forms import ProjetoForm
from .forms import TecnologiaForm


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
