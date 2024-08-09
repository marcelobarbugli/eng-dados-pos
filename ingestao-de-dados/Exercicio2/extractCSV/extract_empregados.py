import os
import pandas as pd
import json

# Diretórios contendo os arquivos CSV
diretorios = {
    'diretorio1': r'\Dados\Empregados' # Caso necessário, insira aqui o caminho para o primeiro diretório!
}

# Estrutura de colunas padrão com CNPJ
colunas_padrao_empregados_cnpj = [
    'employer_name', 'reviews_count', 'culture_count', 'salaries_count',
    'benefits_count', 'employer-website', 'employer-headquarters',
    'employer-founded', 'employer-industry', 'employer-revenue', 'url',
    'Geral', 'Cultura e valores', 'Diversidade e inclusão',
    'Qualidade de vida', 'Alta liderança', 'Remuneração e benefícios',
    'Oportunidades de carreira', 'Recomendam para outras pessoas(%)',
    'Perspectiva positiva da empresa(%)', 'CNPJ', 'Nome', 'match_percent'
]

# Estrutura de colunas padrão com Segmento
colunas_padrao_empregados_seg = [
    'employer_name', 'reviews_count', 'culture_count', 'salaries_count',
    'benefits_count', 'employer-website', 'employer-headquarters',
    'employer-founded', 'employer-industry', 'employer-revenue', 'url',
    'Geral', 'Cultura e valores', 'Diversidade e inclusão',
    'Qualidade de vida', 'Alta liderança', 'Remuneração e benefícios',
    'Oportunidades de carreira', 'Recomendam para outras pessoas(%)',
    'Perspectiva positiva da empresa(%)', 'Segmento', 'Nome', 'match_percent'
]

# Função para carregar arquivos CSV de um diretório e garantir conformidade com as colunas padrão
def carregar_csvs_empregados(diretorio):
    df_acumulado = pd.DataFrame()  # Cria DataFrame vazio
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho_completo = os.path.join(diretorio, arquivo)
            try:
                # Tenta carregar o CSV com diferentes codificações
                try:
                    df = pd.read_csv(caminho_completo, encoding='utf-8', delimiter='|', on_bad_lines='skip')
                except UnicodeDecodeError:
                        try:
                            # Tentar ler com ISO-8859-1
                            print(f"Erro de codificação com UTF-8 para {caminho_completo}. Tentando com 'iso-8859-1'.")
                            df = pd.read_csv(caminho_completo, encoding='iso-8859-1', delimiter='|', on_bad_lines='skip')
                            
                        except UnicodeError:
                                # Tentar ler com Windows-1252
                                print(f"Erro de codificação com UTF-8 para {caminho_completo}. Tentando com 'cp1252'.")
                                df = pd.read_csv(caminho_completo, encoding='cp1252', delimiter='|', on_bad_lines='skip')
                except:
                    pass
                
                # Determinar a estrutura de colunas e aplicar colunas padrão
                if 'CNPJ' in df.columns:
                    colunas_padrao = colunas_padrao_empregados_cnpj
                elif 'Segmento' in df.columns:
                    colunas_padrao = colunas_padrao_empregados_seg
                else:
                    print(f"Erro: Estrutura de colunas desconhecida para {arquivo}.")
                    continue  # Pula para o próximo arquivo
                
                # Ajustar colunas faltantes
                for coluna in colunas_padrao:
                    if coluna not in df.columns:
                        df[coluna] = None  # Adiciona coluna faltante com valor padrão None
                
                # Assegurar que 'CNPJ' seja tratado como inteiro
                if 'CNPJ' in df.columns:
                    df['CNPJ'] = df['CNPJ'].fillna(0).astype(str).replace(0, 'null')
                
                # Ordena as colunas de acordo com o padrão
                df = df[colunas_padrao]
                
                # Acumular DataFrame no df_acumulado
                df_acumulado = pd.concat([df_acumulado, df], ignore_index=True)
                print(f"Carregado {arquivo} de {diretorio} com {len(df)} linhas.")
            except Exception as e:
                print(f"Erro ao carregar {caminho_completo}: {e}")
    return df_acumulado

# Carregar e ajustar CSVs do diretório de empregados
empregados_df = carregar_csvs_empregados(diretorios['diretorio1'])

# Verificar e exibir o DataFrame final
if not empregados_df.empty:
    print("Conteúdo de empregados_df:")
    print(empregados_df.head())

    # Substituir valores None por 'null' no DataFrame
    empregados_df.fillna('null', inplace=True)

    # Convertendo o DataFrame para um dicionário
    empregados_dict = empregados_df.to_dict(orient='records')

    # Convertendo o dicionário para JSON
    empregados_json = json.dumps(empregados_dict, ensure_ascii=False, indent=4)

    # Exibindo o JSON resultante
    print(empregados_json)

    # Opcionalmente, salvar o JSON em um arquivo
    with open('data/bronze/empregados.json', 'w', encoding='utf-8') as json_file:
        json_file.write(empregados_json)
else:
    print("Erro: Nenhum dado foi carregado de 'diretorio1'.")