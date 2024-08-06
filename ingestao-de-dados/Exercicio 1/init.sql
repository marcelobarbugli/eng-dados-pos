-- Connect to database
CREATE DATABASE ingestao;

\c ingestao

CREATE TABLE IF NOT EXISTS reclamacoes (
	id SERIAL PRIMARY KEY,
	Ano SMALLINT,
	Trimestre VARCHAR(2),
	Categoria VARCHAR(100),
	Tipo VARCHAR(20),
	CNPJ_IF VARCHAR(20),
	Instituicao_financeira VARCHAR(255),
	Indice VARCHAR(10),
	Quantidade_de_reclamacoes_reguladas_procedentes INTEGER,
	Quantidade_de_reclamacoes_reguladas___outras INTEGER,
	Quantidade_de_reclamacoes_nao_reguladas INTEGER,
	Quantidade_total_de_reclamacoes INTEGER,
	Quantidade_total_de_clientes_CCS_e_SCR VARCHAR(10),
	Quantidade_de_cliente_CCS VARCHAR(10),
	employer_name VARCHAR(255),
	reviews_count INTEGER,
	culture_count INTEGER,
	salaries_count INTEGER,
	benefits_count INTEGER,
	employer_website VARCHAR(255),
	employer_headquarters VARCHAR(255),
	employer_founded SMALLINT,
	employer_industry VARCHAR(100),
	employer_revenue VARCHAR(100),
	url VARCHAR(200),
	Geral REAL,
	Cultura_e_valores REAL,
	Diversidade_e_inclusao REAL,
	Qualidade_de_vida REAL,
	Alta_lideranca Real,
	Remuneracao_e_beneficios REAL,
	Oportunidades_de_carreira REAL,
	Recomendam_para_outras_pessoas REAL,
	Perspectiva_positiva_da_empresa REAL,
	Segmento VARCHAR(2),
	Nome VARCHAR(255),
	Match_percent SMALLINT,
	CNPJ VARCHAR(30)
);
	
