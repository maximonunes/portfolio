from django.db import models

# 1. CURSO / LICENCIATURA
class Curso(models.Model):
    codigo = models.IntegerField(primary_key=True, help_text="Ex: 260")
    nome = models.CharField(max_length=200)
    grau = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    logotipo = models.ImageField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return self.nome

# 2. UNIDADE CURRICULAR (UC)
class UnidadeCurricular(models.Model):
    codigo_legivel = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='ucs')
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    docente_responsavel = models.CharField(max_length=100, blank=True)
    link_lusofona = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"

# 3. TECNOLOGIA
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=20, blank=True, null=True)
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_oficial = models.URLField(blank=True)
    categoria = models.CharField(max_length=100, help_text="Ex: Frontend, Backend, Linguagem")
    nivel_interesse = models.IntegerField(default=1, help_text="1 a 5")
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

# 4. TRABALHO FINAL DE CURSO (TFC) - Preparado para o teu JSON
class TFC(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)
    orientadores = models.CharField(max_length=255)
    ano_realizacao = models.IntegerField()
    resumo = models.TextField()
    link_pdf = models.URLField(blank=True, null=True)
    link_imagem = models.URLField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='tfcs')

    def __str__(self):
        return self.titulo

# 5. PROJETO (Desenvolvido por ti nas UCs)
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    ano = models.IntegerField()
    link_github = models.URLField(blank=True)
    # Relações
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.titulo

# 6. FORMAÇÃO
class Formacao(models.Model):
    instituicao = models.CharField(max_length=200)
    curso_ou_certificado = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.curso_ou_certificado

# 7. COMPETÊNCIA
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(help_text="1 a 5")
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome

# 8. INTERESSE (Entidade Adicional para valorizar a nota)
class Interesse(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    icone = models.CharField(max_length=50, blank=True, help_text="Ex: fa-gamepad")

    def __str__(self):
        return self.titulo

# 9. MAKING OF (OBRIGATÓRIO)
class MakingOf(models.Model):
    etapa = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    decisoes = models.TextField()
    erros_solucoes = models.TextField(blank=True)
    imagem_caderno = models.ImageField(upload_to='makingof/')
    uso_ia = models.TextField(blank=True)

    def __str__(self):
        return self.etapa