import json
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

# Função para corrigir o JSON
def fix_json(input_file, output_file):
    with open(input_file, 'r', encoding='cp1252') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='cp1252') as outfile:
        for i, line in enumerate(lines):
            line = line.strip()
            if line.endswith("}") and i < len(lines) - 2:
                outfile.write(line + ",\n")
            else:
                outfile.write(line + "\n")
        
    print(f"JSON corrigido salvo em: {output_file}")

# Função para carregar e processar o JSON e salvar como Parquet
def process_json_to_parquet(json_path):
    # Carregar os dados JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Converter o JSON em um DataFrame
    df = pd.DataFrame(data)

    # Substituir 'null' por None para tratamento correto de valores nulos
    df.replace('null', None, inplace=True)

    # Validação e Conversão de Tipos
    try:
        df['employer-founded'] = pd.to_numeric(df['employer-founded'], errors='coerce')
    except Exception as e:
        print(f"Erro ao converter employer-founded: {e}")

    # Adicionar Metadados
    df['ingestion_date'] = datetime.now()
    df['schema_version'] = 1.0  # Versão inicial do schema

    # Criação de logs de validação
    def validate_data(row):
        if not row['employer_name']:
            return 'Missing employer_name'
        if row['reviews_count'] is None or row['reviews_count'] < 0:
            return 'Invalid reviews_count'
        return 'Valid'

    df['validation_status'] = df.apply(validate_data, axis=1)

    # Filtrar registros válidos (se necessário)
    valid_df = df[df['validation_status'] == 'Valid']

    # Converter o DataFrame em uma tabela PyArrow
    table = pa.Table.from_pandas(valid_df)

    # # Gerar um nome de arquivo único usando o timestamp atual
    # timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # parquet_file_path = f'data/silver/empregados_{timestamp}.parquet'

    txt_file_path = os.path.join(f'data/silver/empregados.txt')
    # Escrever a tabela em um arquivo Parquet/TXT
    pq.write_table(table, txt_file_path)

    # print(f"Arquivo Parquet salvo em: {txt_file_path}")
    
    # Ler o arquivo Parquet/TXT em um DataFrame do Pandas
    df = pq.read_table(txt_file_path).to_pandas()

    # Salvar em TXT (formato personalizado, exemplo separado por tabulações)
    
    valid_df.to_csv(txt_file_path, index=False, sep='\t')
    print(f"Arquivo TXT salvo em: {txt_file_path}")
    
    # Visualizar as primeiras linhas do DataFrame
    print(df.head())

# Caminho para o arquivo JSON
json_file_path = 'data/bronze/empregados.json'
fixed_json_file_path = 'data/bronze/empregados_corrected.json'

# Corrigir o JSON e processar
fix_json(json_file_path, fixed_json_file_path)
process_json_to_parquet(fixed_json_file_path)
