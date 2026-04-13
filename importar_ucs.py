import json
import os
import sys
import django

# 1. Configuração do Django
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") 
django.setup()

# Importamos também o modelo Docente
from portfolio.models import Curso, UnidadeCurricular, Docente

def carregar_dados():
    caminho_projeto = os.getcwd()
    # Mantive a pasta 'files' que indicaste que estavas a usar
    pasta_data = os.path.join(caminho_projeto, 'files')
    
    print(f"[*] A procurar ficheiros em: {pasta_data}")

    if not os.path.exists(pasta_data):
        print(f"[!] Erro: A pasta '{pasta_data}' não existe!")
        return

    # Garante que existe pelo menos um docente genérico na DB para não dar erro
    docente_generico, _ = Docente.objects.get_or_create(
        nome="A definir", 
        defaults={'biografia': "Docente por atribuir."}
    )

    ficheiros = [f for f in os.listdir(pasta_data) if f.endswith('.json')]
    print(f"[*] Ficheiros encontrados: {len(ficheiros)}")
    
    contador_sucesso = 0

    for ficheiro in ficheiros:
        caminho_completo = os.path.join(pasta_data, ficheiro)
        
        with open(caminho_completo, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except:
                continue
        
        if 'curricularUnitName' in dados:
            print(f"[*] A processar: {ficheiro}...", end=" ")
            
            # 1. Tratar o Curso
            course_code = dados.get('courseCode')
            if not course_code:
                print("Pular (sem código)")
                continue

            curso, _ = Curso.objects.get_or_create(
                codigo=int(course_code),
                defaults={
                    'nome': dados.get('courseName', 'Curso Desconhecido'),
                    'grau': dados.get('diplomaDegree', 'Licenciatura'),
                }
            )

            
            codigo_uc = dados.get('curricularIUnitReadableCode') or dados.get('curricularUnitReadableCode') or f"UC-{dados.get('curricularUnitCode')}"

            
            uc, criada = UnidadeCurricular.objects.update_or_create(
                codigo_legivel=codigo_uc,
                defaults={
                    'nome': dados.get('curricularUnitName'),
                    'ano': int(dados.get('curricularYear', 1)),
                    'semestre': 1,
                    'ects': float(dados.get('ects', 0)),
                    'curso': curso,
                    'docente_responsavel': docente_generico, 
                    'link_lusofona': f"https://www.ulusofona.pt/programas/{codigo_uc}"
                }
            )
            contador_sucesso += 1
            print("OK!")

    print(f"\n--- Concluído! {contador_sucesso} UCs atualizadas com a nova estrutura. ---")

if __name__ == '__main__':
    carregar_dados()