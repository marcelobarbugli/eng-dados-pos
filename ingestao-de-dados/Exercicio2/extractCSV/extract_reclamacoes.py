import os
import pandas as pd
import json
from config.define import raw_reclamacoes_path, bronze_path


def execute():
    # Diretórios contendo os arquivos CSV
    diretorio = {
        'diretorio1': raw_reclamacoes_path  # Caso necessário, insira aqui o caminho para o primeiro diretório!
    }

    # Estrutura de colunas padrão para reclamações
    colunas_padrao_reclamacoes = [
        'Ano', 'Trimestre', 'Categoria', 'Tipo', 'CNPJ IF', 'Instituição financeira', 'Índice',
        'Quantidade de reclamações reguladas procedentes',
        'Quantidade de reclamações reguladas - outras',
        'Quantidade de reclamações não reguladas',
        'Quantidade total de reclamações',
        'Quantidade total de clientes – CCS e SCR',
        'Quantidade de clientes – CCS',
        'Quantidade de clientes – SCR'
    ]
    # Carregar e ajustar CSVs do diretório de reclamações
    reclamacoes_df = carregar_csvs_reclamacoes(diretorio['diretorio1'], colunas_padrao_reclamacoes)

    # Verificar e exibir o DataFrame final
    if not reclamacoes_df.empty:
        print("Conteúdo de reclamacoes_df:")
        print(reclamacoes_df.head())

        # Substituir valores None por 'null' no DataFrame
        reclamacoes_df.fillna('null', inplace=True)

        # Convertendo o DataFrame para um dicionário
        reclamacoes_dict = reclamacoes_df.to_dict(orient='records')

        # Convertendo o dicionário para JSON
        reclamacoes_json = json.dumps(reclamacoes_dict, ensure_ascii=False, indent=4)

        # Exibindo o JSON resultante
        print(reclamacoes_json)

        # Opcionalmente, salvar o JSON em um arquivo
        output_path = os.path.join(f'{bronze_path}/reclamacoes.json')
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json_file.write(reclamacoes_json)
        print(f"Arquivo JSON salvo em: {output_path}")
    else:
        print("Erro: Nenhum dado foi carregado de 'diretorio Reclamacao'.")

# Função para carregar arquivos CSV de um diretório e garantir conformidade com as colunas padrão
def carregar_csvs_reclamacoes(diretorio, colunas_padrao_reclamacoes):
    df_acumulado = pd.DataFrame()  # Cria DataFrame vazio
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho_completo = os.path.join(diretorio, arquivo)
            try:
                # Tenta carregar o CSV com diferentes codificações e delimitadores
                try:
                    df = pd.read_csv(caminho_completo, encoding='utf-8', delimiter=';', on_bad_lines='skip')
                except UnicodeDecodeError:
                    print(f"Erro de codificação com UTF-8 para {caminho_completo}. Tentando com 'cp1252'.")
                    df = pd.read_csv(caminho_completo, encoding='cp1252', delimiter=';', on_bad_lines='skip')
                
                # Converter 'CNPJ IF' para string
                if 'CNPJ IF' in df.columns:
                    df['CNPJ IF'] = df['CNPJ IF'].astype(str).str.strip()
                
                # Ajustar colunas faltantes para seguir a estrutura padrão
                for coluna in colunas_padrao_reclamacoes:
                    if coluna not in df.columns:
                        df[coluna] = None  # Adiciona coluna faltante com valor padrão None
                        
                # Ordena as colunas de acordo com o padrão
                df = df[colunas_padrao_reclamacoes]
                
                # Acumular DataFrame no df_acumulado
                df_acumulado = pd.concat([df_acumulado, df], ignore_index=True)
                print(f"Carregado {arquivo} de {diretorio} com {len(df)} linhas.")
            except Exception as e:
                print(f"Erro ao carregar {caminho_completo}: {e}")
    return df_acumulado

