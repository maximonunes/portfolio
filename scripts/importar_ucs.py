import json
import os
import sys
import django

# 1. Configuração do ambiente Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") # Verifique se o nome é 'config'
django.setup()

from portfolio.models import Curso, UnidadeCurricular

def carregar_dados():
    # Pasta 'data' no diretório base do projeto
    pasta = os.path.join(BASE_DIR, 'data')
    
    if not os.path.exists(pasta):
        print(f"Erro: Pasta '{pasta}' não encontrada.")
        return

    print("A iniciar importação...")

    # Percorrer todos os ficheiros na pasta 'data'
    for ficheiro in os.listdir(pasta):
        # Lemos apenas a versão em português das APIs da Lusófona
        if ficheiro.endswith('-PT.json'):
            caminho = os.path.join(pasta, ficheiro)
            
            with open(caminho, encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    print(f"Erro ao ler {ficheiro}. Ignorando.")
                    continue
            
            # Verificar se é um ficheiro de UC (baseado na estrutura da API)
            if 'curricularUnitName' in dados:
                
                # 1. Obter ou criar o Curso
                # O seu modelo usa 'codigo' como Primary Key
                course_code = dados.get('courseCode')
                
                if not course_code:
                    print(f"Aviso: Ficheiro {ficheiro} não tem 'courseCode'.")
                    continue

                curso, created = Curso.objects.get_or_create(
                    codigo=int(course_code),
                    defaults={
                        'nome': dados.get('courseName', 'Curso Desconhecido'),
                        'grau': dados.get('diplomaDegree', 'Licenciatura'),
                        'descricao': "" # O seu model tem este campo
                    }
                )

                # 2. Obter ou criar a Unidade Curricular
                # No seu model os campos são: codigo_legivel, nome, ano, semestre, ects, curso
                uc, uc_criada = UnidadeCurricular.objects.update_or_create(
                    codigo_legivel=dados.get('curricularUnitReadableCode', ''),
                    defaults={
                        'nome': dados.get('curricularUnitName', 'UC Sem Nome'),
                        'ano': int(dados.get('curricularYear', 1)),
                        'semestre': int(dados.get('semester', 1)),
                        'ects': float(dados.get('ects', 0)),
                        'curso': curso
                    }
                )

                status = "Criada" if uc_criada else "Atualizada"
                print(f"- {status} UC: {uc.nome} ({curso.nome})")

    print("\nCursos e UCs processados com sucesso!")

if __name__ == '__main__':
    carregar_dados()