import json
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from portfolio.models import TFC, Curso, Autor


def carregar_dados():
    pasta = os.path.join(BASE_DIR, 'data')

    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith('.json'):

            caminho = os.path.join(pasta, ficheiro)

            with open(caminho, encoding='utf-8') as f:
                dados = json.load(f)

            lista_tfcs = dados if isinstance(dados, list) else [dados]
            for item in lista_tfcs:
                # AGORA USAMOS 'item' em vez de 'dados'
                titulo = item.get('title', 'Sem título')
                ano = item.get('year', 0)
                resumo = item.get('summary', '')

                curso_nome = item.get('course', 'Desconhecido')
                autor_nome = item.get('author', 'Desconhecido')

                # Criar ou obter as relações
                curso, _ = Curso.objects.get_or_create(nome=curso_nome)
                autor, _ = Autor.objects.get_or_create(nome=autor_nome)

                # Criar o TFC
                TFC.objects.create(
                    titulo=titulo,
                    ano=ano,
                    resumo=resumo,
                    curso=curso,
                    autor=autor
                )

    print("TFCs carregados com sucesso!")


if __name__ == '__main__':
    carregar_dados()