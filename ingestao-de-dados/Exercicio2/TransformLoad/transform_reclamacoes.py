import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
import os

def process_json_to_parquet(json_path, output_dir):
    # Carregar o JSON completo
    with open(json_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            return

    # Verificar se o arquivo JSON contém uma lista de objetos
    if isinstance(data, list):
        # Converter o JSON em um DataFrame
        df = pd.DataFrame(data)
    else:
        print("Formato de JSON inválido. Esperado uma lista de objetos.")
        return

    # Substituir 'null' por None para tratamento correto de valores nulos
    df.replace('null', None, inplace=True)

    # Renomear 'Área' para 'CNPJ' se essa coluna existir
    if 'Área' in df.columns:
        df.rename(columns={'Área': 'CNPJ'}, inplace=True)
    else:
        print("A coluna 'Área' não foi encontrada no DataFrame para renomear para 'CNPJ'.")

    # Transformar todas as colunas em strings, exceto 'Ano'
    for column in df.columns:
        if column != 'Ano':
            df[column] = df[column].astype(str)

    # Adicionar Metadados
    df['ingestion_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['schema_version'] = 1.0  # Versão inicial do schema

    # Criação de logs de validação
    def validate_data(row):
        if pd.isnull(row['Ano']):
            return 'Missing Ano'
        if pd.isnull(row['Trimestre']):
            return 'Missing Trimestre'
        return 'Valid'

    df['validation_status'] = df.apply(validate_data, axis=1)

    # Filtrar registros válidos (se necessário)
    valid_df = df[df['validation_status'] == 'Valid']

    # Converter o DataFrame em uma tabela PyArrow
    table = pa.Table.from_pandas(valid_df)

    # # Gerar um nome de arquivo único usando o timestamp atual
    # timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # parquet_file_path = os.path.join(output_dir, f'reclamacoes_{timestamp}.parquet')

    # # Criar o diretório de saída se não existir
    # os.makedirs(output_dir, exist_ok=True)

    # # Escrever a tabela em um arquivo Parquet
    # pq.write_table(table, parquet_file_path)
    # print(f"Arquivo Parquet salvo em: {parquet_file_path}")
    
    # Salvar em TXT (formato personalizado, exemplo separado por vírgulas)
    txt_file_path = os.path.join(output_dir, f'reclamacoes.txt')
    valid_df.to_csv(txt_file_path, index=False, sep='\t')
    print(f"Arquivo TXT salvo em: {txt_file_path}")

# Caminho para o arquivo JSON
json_file_path = 'data/bronze/reclamacoes.json'
output_directory = 'data/silver'

# Processar o JSON e salvar como Parquet na camada silver
process_json_to_parquet(json_file_path, output_directory)
