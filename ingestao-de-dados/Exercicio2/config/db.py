import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('mydb')
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS dados_finais (
    employer_name TEXT,
    reviews_count INTEGER,
    culture_count INTEGER,
    salaries_count INTEGER,
    benefits_count INTEGER,
    employer_website TEXT,
    employer_headquarters TEXT,
    employer_founded REAL,
    employer_industry TEXT,
    employer_revenue TEXT,
    url TEXT,
    Geral REAL,
    Cultura_e_valores REAL,
    Diversidade_e_inclusao REAL,
    Qualidade_de_vida REAL,
    Alta_lideranca REAL,
    Remuneracao_e_beneficios REAL,
    Oportunidades_de_carreira REAL,
    Recomendam_para_outras_pessoas REAL,
    Perspectiva_positiva_da_empresa REAL,
    CNPJ REAL,
    Nome TEXT,
    match_percent INTEGER,
    Segmento_x TEXT,
    ingestion_date_x TEXT,
    schema_version_x REAL,
    validation_status_x TEXT,
    Segmento_y TEXT,
    ingestion_date_y TEXT,
    schema_version_y REAL,
    validation_status_y TEXT,
    Ano INTEGER,
    Trimestre TEXT,
    Categoria TEXT,
    Tipo TEXT,
    Instituicao_financeira TEXT,
    Indice TEXT,
    Quantidade_de_reclamacoes_reguladas_procedentes INTEGER,
    Quantidade_de_reclamacoes_reguladas_outras INTEGER,
    Quantidade_de_reclamacoes_nao_reguladas INTEGER,
    Quantidade_total_de_reclamacoes INTEGER,
    Quantidade_total_de_clientes_CCS_e_SCR TEXT,
    Quantidade_de_clientes_CCS TEXT,
    Quantidade_de_clientes_SCR TEXT,
    ingestion_date TEXT,
    schema_version REAL,
    validation_status TEXT
)
''')

# Carregar os dados do CSV
df = pd.read_csv('data/gold/dados_finais.csv')

# Inserir os dados na tabela
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO dados_finais VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', tuple(row))

# Confirmar a inserção
conn.commit()

# Fechar a conexão
conn.close()
