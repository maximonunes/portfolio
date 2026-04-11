import json
import os
import sys
import django

# 1. Configuração do ambiente Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Confirma se o teu projeto se chama 'config'
django.setup()

from portfolio.models import TFC, Curso

def carregar_dados():
    # Pasta onde estão os teus ficheiros JSON
    pasta = os.path.join(BASE_DIR, 'data')
    
    if not os.path.exists(pasta):
        print(f"Erro: A pasta {pasta} não foi encontrada.")
        return

    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith('.json'):
            caminho = os.path.join(pasta, ficheiro)
            print(f"A processar: {ficheiro}")

            with open(caminho, encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    print(f"Erro ao ler o ficheiro {ficheiro}. Formato inválido.")
                    continue

            lista_tfcs = dados if isinstance(dados, list) else [dados]
            
            for item in lista_tfcs:
                # Extração de dados do JSON (com valores por defeito)
                titulo = item.get('title', 'Sem título')
                ano = item.get('year', 2024)
                resumo = item.get('summary', '')
                autores_string = item.get('author', 'Autor Desconhecido') # No teu model é CharField
                
                # Dados do Curso
                curso_nome = item.get('course', 'Desconhecido')
                # Nota: O teu model Curso exige um 'codigo' como PK. 
                # Se o JSON não tiver, vamos ter de inventar um ou procurar por nome.
                curso_codigo = item.get('course_id', 999) 

                # 2. Obter ou Criar o Curso (Necessário para a ForeignKey do TFC)
                # Usamos defaults para o caso de o curso ser criado agora
                curso, _ = Curso.objects.get_or_create(
                    codigo=curso_codigo, 
                    defaults={'nome': curso_nome}
                )

                # 3. Criar ou Atualizar o TFC
                # Usamos update_or_create para evitar duplicados se correres o script 2 vezes
                tfc, criado = TFC.objects.update_or_create(
                    titulo=titulo,
                    defaults={
                        'autores': autores_string,
                        'ano_realizacao': ano, # No model é 'ano_realizacao', não 'ano'
                        'resumo': resumo,
                        'curso': curso,
                        'link_repositorio': item.get('repo_link', ''),
                        'link_video': item.get('video_link', '')
                    }
                )

                status = "Criado" if criado else "Atualizado"
                print(f"- {status}: {titulo}")

    print("\nImportação concluída com sucesso!")

if __name__ == '__main__':
    carregar_dados()