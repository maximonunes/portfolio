import json
import os
import sys
import django

# 1. Configuração do Django
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") # <--- CONFIRMA SE É 'project' ou 'portfolio'
django.setup()

from portfolio.models import Curso, UnidadeCurricular

def carregar_dados():
    # Tenta encontrar a pasta 'data' de forma absoluta
    caminho_projeto = os.getcwd()
    pasta_data = os.path.join(caminho_projeto, 'files')
    
    print(f"[*] A procurar ficheiros em: {pasta_data}")

    if not os.path.exists(pasta_data):
        print(f"[!] Erro: A pasta '{pasta_data}' não existe!")
        return

    ficheiros = os.listdir(pasta_data)
    print(f"[*] Ficheiros encontrados na pasta: {len(ficheiros)}")
    
    contador_sucesso = 0

    for ficheiro in ficheiros:
        # Verifica se o ficheiro termina em -PT.json (ajusta se os teus não tiverem o -PT)
        if ficheiro.endswith('.json'):
            print(f"[*] A processar: {ficheiro}...", end=" ")
            caminho_completo = os.path.join(pasta_data, ficheiro)
            
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except Exception as e:
                    print(f"Erro ao ler JSON: {e}")
                    continue
            
            if 'curricularUnitName' in dados:
                # Tratar o Curso
                course_code = dados.get('courseCode')
                if not course_code:
                    print("Pular (sem courseCode)")
                    continue

                curso, _ = Curso.objects.get_or_create(
                    codigo=int(course_code),
                    defaults={
                        'nome': dados.get('courseName', 'Curso Desconhecido'),
                        'grau': dados.get('diplomaDegree', 'Bachelor'),
                    }
                )

                # Tratar Código Legível (com a correção do 'I' extra)
                codigo_uc = dados.get('curricularIUnitReadableCode') or dados.get('curricularUnitReadableCode') or f"UC-{dados.get('curricularUnitCode')}"

                # Criar/Atualizar UC
                uc, criada = UnidadeCurricular.objects.update_or_create(
                    codigo_legivel=codigo_uc,
                    defaults={
                        'nome': dados.get('curricularUnitName'),
                        'ano': int(dados.get('curricularYear', 1)),
                        'semestre': 1, # Podes ajustar a lógica aqui
                        'ects': float(dados.get('ects', 0)),
                        'curso': curso,
                        'docente_responsavel': "Consultar Ficha",
                        'link_lusofona': f"https://www.ulusofona.pt/programas/{codigo_uc}"
                    }
                )
                contador_sucesso += 1
                print("OK!")
            else:
                print("Ignorado (não é formato de UC)")

    print(f"\n--- Concluído! {contador_sucesso} UCs processadas. ---")

if __name__ == '__main__':
    carregar_dados()