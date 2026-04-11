from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    ano = models.IntegerField()
    resumo = models.TextField()

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class UnidadeCurricular(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    ects = models.FloatField()
    semestre = models.IntegerField()

    def __str__(self):
        return self.nome
