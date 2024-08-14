from sqlite3 import connect
from sqlalchemy import create_engine
import unidecode
import pandas as pd
from config.define import mysql, gold_path, silver_path

def normalize_header(header: str):
    if header == 'Instituição financeira':
        header = 'nome'
    if header == "CNPJ IF":
        header = "CNPJ"
    if header != 'CNPJ':
        header = header.lower().replace('–', '_').replace('-', '_').replace('  ', '_').replace(' ', '_').replace('__', '')
    return header

def normalize_column(df):
    newDf = df
    newDf.columns = [unidecode.unidecode(normalize_header(col)) for col in df.columns]
    return newDf

def load_mysql(df, mysql_info):
    conn =  create_engine(f'mysql+mysqlconnector://{mysql_info['user']}:{mysql_info['password']}@{mysql_info['host']}/{mysql_info['database']}')
    df.to_sql('dados_finais_v2', conn, if_exists='replace', index=False)

def load_sqlite(df, db_path='database.sqlite'):
    conn = connect(db_path)
    df.to_sql('dados_finais_v2', conn, if_exists='replace', index=False)
    conn.close()


def execute():
    df_bancos = normalize_column(pd.read_csv(filepath_or_buffer=f'{silver_path}/bancos.txt', sep='\t', dtype=str))
    df_empregados = normalize_column(pd.read_csv(filepath_or_buffer=f'{silver_path}/empregados.txt', sep='\t', dtype=str))
    df_reclamacoes = normalize_column(pd.read_csv(filepath_or_buffer=f'{silver_path}/reclamacoes.txt', sep='\t', dtype=str))

    df_bancos_empregados = pd.concat([df_bancos, df_empregados])

    df_bancos_empregados.to_parquet(f'{gold_path}/bancos_empregados.parquet')

    df_final = pd.merge(df_reclamacoes,df_bancos_empregados, on=['CNPJ', 'nome'], how='inner').drop_duplicates().drop_duplicates(subset=['CNPJ']).drop_duplicates(subset=['nome'])

    df_final.to_parquet(f'{gold_path}/final.parquet')
    
    try: 
        load_mysql(df_final, mysql)
    finally:
        load_sqlite(df_final)




