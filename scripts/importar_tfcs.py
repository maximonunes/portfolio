import json
import os
import sys
import django
import random

# 1. Configuração Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from portfolio.models import TFC, Curso

def carregar_dados():
    caminho_json = os.path.join(BASE_DIR, 'data', 'tfcs.json')
    
    if not os.path.exists(caminho_json):
        print(f"Erro: Ficheiro não encontrado em {caminho_json}")
        return

    with open(caminho_json, encoding='utf-8') as f:
        dados = json.load(f)

    lista_tfcs = dados if isinstance(dados, list) else [dados]

    for item in lista_tfcs:
        # Extrair nome do curso e ano
        info_lic = item.get('licenciatura', '')
        # Tenta tirar "Licenciatura em " para bater certo com o que costuma estar na BD
        nome_curso_json = info_lic.split('.')[0].replace('Licenciatura em ', '').strip() if '.' in info_lic else info_lic
        
        # 1. TENTATIVA DE MATCH (Flexível)
        curso = Curso.objects.filter(nome__icontains=nome_curso_json).first()

        # 2. SE NÃO EXISTIR, CRIA (com código seguro)
        if not curso:
            # Gera um código aleatório alto ou baseado no último para evitar UNIQUE constraint
            ultimo = Curso.objects.order_by('-codigo').first()
            novo_cod = (ultimo.codigo + 1) if (ultimo and ultimo.codigo < 50000) else random.randint(60000, 90000)
            
            curso = Curso.objects.create(
                codigo=novo_cod,
                nome=nome_curso_json,
                grau='Licenciatura'
            )
            print(f"[*] Curso criado automaticamente: {nome_curso_json}")

        # Extrair ano
        ano_final = 2025
        if '.' in info_lic:
            ano_str = ''.join(filter(str.isdigit, info_lic.split('.')[-1]))
            if ano_str: ano_final = int(ano_str)

        # 3. CRIAR O TFC
        tfc, criado = TFC.objects.update_or_create(
            titulo=item.get('titulo'),
            defaults={
                'autores': item.get('autores', 'Anónimo'),
                'ano_realizacao': ano_final,
                'resumo': item.get('resumo', '').replace('Resumo: ', '').strip(),
                'link_video': item.get('link_pdf', ''),
                'curso': curso
            }
        )

        status = "Criado" if criado else "Atualizado"
        print(f"[{status}] {tfc.titulo} -> {curso.nome}")

if __name__ == '__main__':
    carregar_dados()