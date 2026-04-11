import os
import json
import sys
import django

# 1. Configuração do ambiente Django
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from portfolio.models import TFC, Curso

def importar_dados():
    # Caminho para o ficheiro JSON
    ficheiro_path = 'data/tfcs.json'
    
    if not os.path.exists(ficheiro_path):
        print(f"Erro: Ficheiro {ficheiro_path} não encontrado!")
        return

    with open(ficheiro_path, 'r', encoding='utf-8') as f:
        tfcs_data = json.load(f)

    for item in tfcs_data:
        # 1. Tratar o Curso (pega apenas o nome antes do ponto)
        # Ex: "Licenciatura em Engenharia Informática. 2025" -> "Licenciatura em Engenharia Informática"
        nome_completo = item.get('licenciatura', 'Curso Desconhecido')
        nome_curso = nome_completo.split('.')[0].strip()

        # Tenta encontrar o curso, se não existir cria com um código genérico
        curso = Curso.objects.filter(nome__icontains=nome_curso).first()

        if not curso:
            # Usamos um código alto (ex: 999 + total de cursos) para garantir que é único
            novo_codigo = 1000 + Curso.objects.count()
            curso = Curso.objects.create(
                nome=nome_curso,
                codigo=novo_codigo,
                grau='Licenciatura'
            )
            print(f"[*] Novo curso criado: {nome_curso} com código {novo_codigo}")
        # 2. Criar ou Atualizar o TFC
        # Usamos o título como identificador único para não duplicar
        tfc, criado = TFC.objects.update_or_create(
            titulo=item.get('titulo'),
            defaults={
                'autores': item.get('autores', 'Autor Desconhecido'),
                'orientadores': item.get('orientadores', 'Não indicado'),
                'ano_realizacao': 2025,
                'resumo': item.get('resumo', ''),
                'link_pdf': item.get('link_pdf') if item.get('link_pdf') != "Sem PDF" else None,
                'link_imagem': item.get('link_imagem', ''),
                'rating': item.get('rating', 0),
                'curso': curso
            }
        )

        status = "Criado" if criado else "Atualizado"
        print(f"[{status}] {tfc.titulo}")

if __name__ == "__main__":
    print("A iniciar importação...")
    importar_dados()
    print("Importação concluída!")