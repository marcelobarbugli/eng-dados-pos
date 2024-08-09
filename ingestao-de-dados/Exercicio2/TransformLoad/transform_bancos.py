import json
import pandas as pd
import os
from datetime import datetime

def fix_json(input_file, output_file):
    with open(input_file, 'r', encoding='cp1252') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='cp1252') as outfile:
        outfile.write("[\n")
        for i, line in enumerate(lines):
            line = line.strip()
            if line.endswith("}") and i < len(lines) - 1:
                outfile.write(line + ",\n")
            else:
                outfile.write(line + "\n")
        outfile.write("]\n")
        
    print(f"JSON corrigido salvo em: {output_file}")

input_file = 'data/bronze/bancos.json'
output_file = 'data/bronze/bancos_corrected.json'
fix_json(input_file, output_file)

def process_json_to_csv_parquet_and_txt(json_path, output_dir):
    with open(json_path, 'r', encoding='cp1252') as file:
        data = json.load(file)

    if not data:
        print("JSON limpo está vazio.")
        return

    df = pd.DataFrame(data)
    df.replace('null', None, inplace=True)

    if 'Nome' in df.columns:
        df['Nome'] = df['Nome'].str.replace('- PRUDENCIAL', '', regex=False)
    else:
        print("Aviso: Coluna 'Nome' não encontrada no DataFrame.")

    if 'CNPJ' in df.columns:
        df['CNPJ'] = df['CNPJ'].astype(str)
    else:
        print("Aviso: Coluna 'CNPJ' não encontrada no DataFrame.")

    df['ingestion_date'] = datetime.now()
    df['schema_version'] = 1.0

    def validate_data(row):
        if 'Nome' not in row or not row['Nome']:
            return 'Missing Nome'
        if 'CNPJ' not in row or not row['CNPJ']:
            return 'Invalid CNPJ'
        return 'Valid'

    if 'Nome' in df.columns and 'CNPJ' in df.columns:
        df['validation_status'] = df.apply(validate_data, axis=1)
        valid_df = df[df['validation_status'] == 'Valid']
    else:
        print("Aviso: Colunas necessárias para validação não encontradas.")
        valid_df = df

    # Gerar um nome de arquivo único usando o timestamp atual
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Salvar em TXT (formato personalizado, exemplo separado por tabulações)
    txt_file_path = os.path.join(output_dir, f'bancos.txt')
    valid_df.to_csv(txt_file_path, index=False, sep='\t')
    print(f"Arquivo TXT salvo em: {txt_file_path}")

    # Visualizar as primeiras linhas do DataFrame
    print(valid_df.head())

json_file_path = 'data/bronze/bancos_corrected.json'
output_directory = 'data/silver'
process_json_to_csv_parquet_and_txt(json_file_path, output_directory)
