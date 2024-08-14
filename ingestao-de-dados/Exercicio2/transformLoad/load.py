import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import unidecode
from config.define import silver_path, gold_path, mysql


def read_text_files():
    # Paths to the text files
    path_empregados = f'{silver_path}/empregados.txt'
    path_bancos = f'{silver_path}/bancos.txt'
    path_reclamacoes = f'{silver_path}/reclamacoes.txt'
    
    # Read text files with specific encoding
    df_empregados = pd.read_csv(path_empregados, delimiter='\t', encoding='utf-8')
    df_bancos = pd.read_csv(path_bancos, delimiter='\t', encoding='cp1252')
    df_reclamacoes = pd.read_csv(path_reclamacoes, delimiter='\t', encoding='utf-8')
    
    # Rename 'CNPJ IF' to 'CNPJ' in df_reclamacoes
    df_reclamacoes.rename(columns={'CNPJ IF': 'CNPJ'}, inplace=True)
    
    return df_empregados, df_bancos, df_reclamacoes

def clean_cnpj(df):
    # Convert 'CNPJ' column to string and remove any '.0'
    df['CNPJ'] = df['CNPJ'].astype(str).str.replace('.0', '', regex=False).str.strip()
    df['CNPJ'] = df['CNPJ'].astype(str).str.replace('nan', '', regex=False).str.strip()
    df.dropna(subset=['CNPJ'], inplace=True)
    return df

def update_cnpj_based_on_name(df_empregados, df_bancos):
    # Create a dictionary of Nome to CNPJ from df_empregados
    name_to_cnpj = pd.Series(df_empregados['CNPJ'].values, index=df_empregados['Nome']).to_dict()
    
    # Update df_bancos['CNPJ'] where df_bancos['Nome'] exists in df_empregados['Nome']
    df_bancos['CNPJ'] = df_bancos['Nome'].map(name_to_cnpj).fillna(df_bancos['CNPJ'])
    
    return df_bancos

def normalize_and_merge(df_empregados, df_bancos, df_reclamacoes):
    # Normalize names to uppercase
    df_empregados['Nome'] = df_empregados['Nome'].str.upper()
    df_empregados['employer_name'] = df_empregados['employer_name'].str.upper()
    df_bancos['Nome'] = df_bancos['Nome'].str.upper()
    
    # Clean and format CNPJ columns
    df_empregados = clean_cnpj(df_empregados)
    df_bancos = clean_cnpj(df_bancos)
    ddf_bancos = update_cnpj_based_on_name(df_empregados, df_bancos)
    df_reclamacoes = clean_cnpj(df_reclamacoes)

    # Merge empregados and bancos using CNPJ
    df_merged = pd.merge(df_empregados, df_bancos, on=['CNPJ', 'Nome'], how='inner')

    # Merge with reclamacoes using CNPJ
    df_final = pd.merge(df_merged, df_reclamacoes, on='CNPJ', how='inner')

    print("Schema of df_merged:")
    df_final.info()
    # Drop duplicates across all columns
    df_final = df_final.drop_duplicates()

    return df_final



def load_into_sqlite(csv_path, db_path='database.sqlite'):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(csv_path)
    df.to_sql('dados_finais', conn, if_exists='replace', index=False)
    conn.close()

def load_into_mysql(csv_path, mysql_info):
    conn =  create_engine(f'mysql+mysqlconnector://{mysql_info['user']}:{mysql_info['password']}@{mysql_info['host']}/{mysql_info['database']}')
    df = pd.read_csv(csv_path)
    df.columns = [unidecode.unidecode(col).replace('-', '') for col in df.columns]
    df.columns = [unidecode.unidecode(col).replace(' ', '_') for col in df.columns]
    df.columns = [unidecode.unidecode(col).replace('__', '_') for col in df.columns]

    df.to_sql('dados_finais', conn, if_exists='replace', index=False)

def main():
    df_empregados, df_bancos, df_reclamacoes = read_text_files()
    df_final = normalize_and_merge(df_empregados, df_bancos, df_reclamacoes)
    print(df_final.head())
    
    # Save the final DataFrame to a CSV file
    csv_path = f'{gold_path}/dados_finais.csv'
    df_final.to_csv(csv_path, index=False)
    
    # Load the data into SQLite
    load_into_sqlite(csv_path)
    
    # Load the data into SQLite
    load_into_mysql(csv_path, mysql)