"""Configuration File"""

dados_path = r'./Dados'

raw_empregados_path = rf'{dados_path}/Empregados'

raw_bancos_path = rf'{dados_path}/Bancos'

raw_reclamacoes_path = rf'{dados_path}/Reclamacoes'

data_path = r'./data'

bronze_path = rf'{data_path}/bronze'

silver_path = rf'{data_path}/silver'

gold_path = rf'{data_path}/gold'

sqlite_path = 'database'

mysql = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'eEDB011'
}