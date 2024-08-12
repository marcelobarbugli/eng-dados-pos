import sqlite3

def execute(db:str):
    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Executar a consulta SQL
    cursor.execute("SELECT * FROM dados_finais limit 10")

    # Recuperar todos os resultados da consulta
    resultados = cursor.fetchall()
    print(resultados)

    # # Se desejar, converter os resultados em um DataFrame do pandas
    # colunas = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
    # df = pd.DataFrame(resultados, columns=colunas)

    # # Exibir o DataFrame
    # print(df)

    # Fechar a conexão
    conn.close()
