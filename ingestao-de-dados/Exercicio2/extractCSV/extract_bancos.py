import os
import pandas as pd

# Diretório contendo o arquivo TSV
diretorio = r'\Dados\Bancos\EnquadramentoInicia_v2.tsv' # Caso necessário, insira aqui o caminho para o primeiro diretório!
# Caminho completo para o arquivo TSV
caminho_completo = os.path.join(diretorio)
# Diretório onde o JSON será salvo
output_directory = r'\data\bronze'

# Estrutura de colunas padrão baseada nas colunas do TSV
colunas_padrao = [
    'Segmento', 'CNPJ', 'Nome'
]

# Função para carregar o arquivo TSV
def carregar_tsv(caminho_arquivo, colunas_padrao):
    try:
        df = pd.read_csv(caminho_arquivo, encoding='utf-8', delimiter='\t', on_bad_lines='skip')
    except UnicodeDecodeError:
        try:
            # Tentar ler com ISO-8859-1
            print(f"Erro de codificação com UTF-8 para {caminho_arquivo}. Tentando com 'iso-8859-1'.")
            df = pd.read_csv(caminho_arquivo, encoding='iso-8859-1', delimiter='\t', on_bad_lines='skip')
        except UnicodeError:
            # Tentar ler com Windows-1252
            print(f"Erro de codificação com iso-8859-1 para {caminho_arquivo}. Tentando com 'cp1252'.")
            df = pd.read_csv(caminho_arquivo, encoding='cp1252', delimiter='\t', on_bad_lines='skip')
        
    # Aplicar trim em todas as colunas de string
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Remover a substring "- PRUDENCIAL" da coluna "Nome" e aplicar trim
    df['Nome'] = df['Nome'].str.replace('- PRUDENCIAL', '', regex=False).str.strip()
    # Converter CNPJ para string e aplicar trim
    if 'CNPJ' in df.columns:
        df['CNPJ'] = df['CNPJ'].astype(str).str.strip()

    # Ordenar as colunas de acordo com o padrão
    df = df[colunas_padrao]

    print(f"Carregado {caminho_arquivo} com {len(df)} linhas.")
    return df

# Verificar se o diretório de saída existe, criá-lo se não existir
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Carregar o TSV
df = carregar_tsv(caminho_completo, colunas_padrao)
if not df.empty:
    print("Conteúdo do DataFrame:")
    print(df.head())

    # Caminho para salvar o JSON
    json_file_path = os.path.join(output_directory, r'\data\bronze\bancos.json')

    # Salvar o DataFrame em um arquivo JSON
    df.to_json(json_file_path, orient='records', lines=True, force_ascii=False)
    print(f"Arquivo JSON salvo em: {json_file_path}")
else:
    print("Erro: Nenhum dado foi carregado.")
