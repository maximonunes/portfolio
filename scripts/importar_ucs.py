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
    pasta = os.path.join(BASE_DIR, 'data')
    
    if not os.path.exists(pasta):
        print(f"Erro: Pasta '{pasta}' não encontrada.")
        return

    print("A iniciar importação de UCs...")

    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith('-PT.json'):
            caminho = os.path.join(pasta, ficheiro)
            
            with open(caminho, encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    continue
            
            if 'curricularUnitName' in dados:
                # 1. Curso
                course_code = dados.get('courseCode')
                if not course_code: continue

                curso, _ = Curso.objects.get_or_create(
                    codigo=int(course_code),
                    defaults={
                        'nome': dados.get('courseName', 'Curso Desconhecido'),
                        'grau': dados.get('diplomaDegree', 'Licenciatura'),
                        'descricao': "" 
                    }
                )

                # 2. Unidade Curricular
                # Tratamento de tipos para evitar erros de validação
                try:
                    ano = int(dados.get('curricularYear', 1))
                    semestre = int(dados.get('semester', 1))
                    ects = float(dados.get('ects', 0))
                except (ValueError, TypeError):
                    ano, semestre, ects = 1, 1, 0

                uc, uc_criada = UnidadeCurricular.objects.update_or_create(
                    codigo_legivel=dados.get('curricularUnitReadableCode', ''),
                    defaults={
                        'nome': dados.get('curricularUnitName', 'UC Sem Nome'),
                        'ano': ano,
                        'semestre': semestre,
                        'ects': ects,
                        'curso': curso
                    }
                )

                status = "Criada" if uc_criada else "Atualizada"
                print(f"- {status} UC: {uc.nome}")

    print("\nImportação concluída!")

if __name__ == '__main__':
    carregar_dados()