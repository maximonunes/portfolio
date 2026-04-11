from django.db import models


class Curso(models.Model):
    codigo = models.IntegerField(primary_key=True, help_text="Código do curso (ex: 260 para LEI)")
    nome = models.CharField(max_length=200)
    grau = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: Licenciatura, Mestrado")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.grau})"


class UnidadeCurricular(models.Model):
    codigo_legivel = models.CharField(max_length=50, unique=True, help_text="Código legível da UC da API")
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return f"{self.nome} ({self.ano}º Ano, {self.semestre}º Semestre)"


# ==========================================
# 2. TRABALHOS FINAIS DE CURSO (TFC)
# ==========================================

class TFC(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.CharField(max_length=255, help_text="Nomes dos autores separados por vírgula")
    ano_realizacao = models.IntegerField()
    resumo = models.TextField()
    link_repositorio = models.URLField(blank=True, null=True)
    link_video = models.URLField(blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='tfcs')

    def __str__(self):
        return f"{self.titulo} ({self.ano_realizacao})"


# ==========================================
# 3. NÚCLEO DO PORTFÓLIO PESSOAL
# ==========================================

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=20, blank=True, null=True)
    # Se preferires usar um URL para a imagem em vez de fazer upload, muda para URLField
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True) 
    categoria = models.CharField(max_length=100, help_text="Ex: Frontend, Backend, Base de Dados")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem_destaque = models.ImageField(upload_to='projetos/', blank=True, null=True)
    ano_realizacao = models.IntegerField()
    link_github = models.URLField(blank=True, null=True)
    link_live = models.URLField(blank=True, null=True)
    
    # Relações
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    instituicao = models.CharField(max_length=200)
    curso_ou_certificado = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True, help_text="Deixar em branco se ainda a decorrer")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.curso_ou_certificado} - {self.instituicao}"


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(help_text="Nível de proficiência (ex: 1 a 5)")

    def __str__(self):
        return f"{self.nome} (Nível {self.nivel})"


class Interesse(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True, help_text="Classe FontAwesome (ex: fa-solid fa-gamepad)")

    def __str__(self):
        return self.titulo