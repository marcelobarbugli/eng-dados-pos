import sqlite3
from config.define import sqlite_path

def execute():
    # Conectar ao banco de dados SQLite
    db_path = sqlite_path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop das views, se existirem
    cursor.execute('DROP VIEW IF EXISTS v_satisfacao_geral;')
    cursor.execute('DROP VIEW IF EXISTS v_reclamacoes_clientes;')
    cursor.execute('DROP VIEW IF EXISTS v_crescimento_empresa;')
    cursor.execute('DROP VIEW IF EXISTS v_comparacao_segmentos;')
    cursor.execute('DROP VIEW IF EXISTS v_indicadores_financeiros;')

    # 1. View para Análise de Satisfação Geral dos Empregados
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS v_satisfacao_geral AS
    SELECT DISTINCT
        employer_name,
        AVG(Geral) AS media_geral,
        AVG(Cultura_e_valores) AS media_cultura_valores,
        AVG(Diversidade_e_inclusao) AS media_diversidade_inclusao,
        AVG(Qualidade_de_vida) AS media_qualidade_vida,
        AVG(Alta_lideranca) AS media_alta_lideranca,
        AVG(Remuneracao_e_beneficios) AS media_remuneracao_beneficios,
        AVG(Oportunidades_de_carreira) AS media_oportunidades_carreira
    FROM
        dados_finais
    GROUP BY
        employer_name;
    ''')

    # 2. View para Análise de Reclamações versus Clientes
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS v_reclamacoes_clientes AS
    SELECT DISTINCT
        Instituicao_financeira,
        Ano,
        Trimestre,
        Quantidade_total_de_reclamacoes,
        CAST(REPLACE(Quantidade_total_de_clientes_CCS_e_SCR, ',', '') AS INTEGER) AS total_clientes,
        Quantidade_total_de_reclamacoes * 1.0 / CAST(REPLACE(Quantidade_total_de_clientes_CCS_e_SCR, ',', '') AS INTEGER) AS reclamacoes_por_cliente
    FROM
        dados_finais
    WHERE
        Quantidade_total_de_clientes_CCS_e_SCR IS NOT NULL
        AND Quantidade_total_de_clientes_CCS_e_SCR != '';
    ''')

    # 3. View para Análise de Crescimento ao Longo do Tempo
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS v_crescimento_empresa AS
    SELECT DISTINCT
        employer_name,
        Ano,
        Trimestre,
        AVG(Geral) AS media_geral,
        AVG(Perspectiva_positiva_da_empresa) AS media_perspectiva_positiva
    FROM
        dados_finais
    GROUP BY
        employer_name, Ano, Trimestre;
    ''')

    # 4. View para Comparação de Segmentos
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS v_comparacao_segmentos AS
    SELECT DISTINCT
        Segmento_x,
        AVG(Geral) AS media_geral,
        AVG(Cultura_e_valores) AS media_cultura_valores,
        AVG(Diversidade_e_inclusao) AS media_diversidade_inclusao,
        AVG(Qualidade_de_vida) AS media_qualidade_vida,
        AVG(Alta_lideranca) AS media_alta_lideranca,
        AVG(Remuneracao_e_beneficios) AS media_remuneracao_beneficios,
        AVG(Oportunidades_de_carreira) AS media_oportunidades_carreira
    FROM
        dados_finais
    GROUP BY
        Segmento_x;
    ''')

    # 5. View para Análise de Indicadores Financeiros
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS v_indicadores_financeiros AS
    SELECT DISTINCT
        Instituicao_financeira,
        Ano,
        Trimestre,
        Indice,
        Quantidade_de_reclamacoes_reguladas_procedentes,
        Quantidade_de_reclamacoes_nao_reguladas,
        Quantidade_total_de_reclamacoes,
        CAST(REPLACE(Quantidade_total_de_clientes_CCS_e_SCR, ',', '') AS INTEGER) AS total_clientes
    FROM
        dados_finais
    WHERE
        Indice IS NOT NULL;
    ''')

    # Confirmar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()
