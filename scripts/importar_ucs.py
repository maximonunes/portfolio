import json
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from portfolio.models import Curso, UnidadeCurricular

def carregar_dados():
    pasta = 'data'
    
    # Percorrer todos os ficheiros na pasta 'files'
    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith('-PT.json'): # Lemos apenas a versão em português
            caminho = os.path.join(pasta, ficheiro)
            
            with open(caminho, encoding='utf-8') as f:
                dados = json.load(f)
            
            # Verificar se é um ficheiro de UC (tem curricularUnitName)
            if 'curricularUnitName' in dados:
                # 1. Obter ou criar o Curso (Licenciatura)
                curso, created = Curso.objects.get_or_create(
                    nome=dados.get('courseName', 'Desconhecido'),
                    defaults={
                        'sigla': str(dados.get('courseCode', '')),
                        'grau': dados.get('diplomaDegree', ''),
                        'duracao_anos': 3,
                        'ects': 180,
                        'descricao': '',
                        'saida_profissional': ''
                    }
                )

                # 2. Obter ou criar a Unidade Curricular
                UnidadeCurricular.objects.update_or_create(
                    codigo=dados.get('curricularIUnitReadableCode', ''),
                    defaults={
                        'nome': dados.get('curricularUnitName', ''),
                        'ano_curricular': dados.get('curricularYear', 1),
                        'semestre': dados.get('semester' , 1), 
                        'ects': dados.get('ects', 0),
                        'descricao': dados.get('presentation', ''),
                        'objetivos': dados.get('objectives', ''),
                        'programa': dados.get('programme', ''),
                        'avaliacao': dados.get('avaliacao', ''),
                        'licenciatura': curso
                    }
                )
    print("Cursos e UCs carregados com sucesso!")

if __name__ == '__main__':
    carregar_dados()