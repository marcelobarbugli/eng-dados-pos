
# Exercício 3 - Engenharia de Dados - Ingestão de Dados

Este repositório contém a solução para o **Exercício 3** da disciplina de Engenharia de Dados, focando em ingestão de dados. O objetivo principal deste exercício é aplicar técnicas de ingestão, transformação e armazenamento de dados utilizando processamento Spark (databricks community) e PostgreSQL.

## Sumário

- [Contexto](#contexto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instruções de Uso](#instruções-de-uso)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuindo](#contribuindo)

## Contexto

Implementar um pipeline de ingestão de dados. Utilizando Python e Spark, o foco é trabalhar com dados de fontes diversas, realizar a transformação necessária e armazená-los de forma eficiente.

## Estrutura do Projeto

```
ingestao-de-dados/
├── data/                   # Diretório de dados de entrada e saída
├── evidencias/              # Notebooks Jupyter utilizados no desenvolvimento
├── scripts/                    # Scripts de processamento e ingestão
│   ├── load_tables.ipynb        # Script principal de ingestão de dados - to Bronze
│   └── transform_raw_data.ipynb   # Script de transformação dos dados - to Silver
│   ├── load_delta_db.ipynb        # Script criação da DeltaTable - to Gold
│   └── LOAD_DF_TO_DB_SQL.ipynb   # Script de carregar dados no PostgreSQL
├── Atividade3.ppt/                  # Apresentação
└── README.md               # Documentação do projeto
```

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.x](https://www.python.org/downloads/)
- [Databricks Community Notebook](https://community.cloud.databricks.com/login.html)
- To be update: Lista de bibliotecas necessárias (listadas em `requirements.txt`)

## Instruções de Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/marcelobarbugli/eng-dados-pos.git
   cd eng-dados-pos/ingestao-de-dados/exercicio3
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o scripts de ingestão de dados:
   ```bash
   python scripts/load_tables.ipynb 
   python scripts/transform_raw_data.ipynb 
   python scripts/load_delta_db.ipynb
   python scripts/LOAD_DF_TO_DB_SQL.ipynb
   ```

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal.
- **Databricks Community Notebook**: Para desenvolvimento interativo e visualização de dados.
- **Apache Spark**: Motor de processamento distribuído utilizado para manipulação e análise de grandes volumes de dados de forma eficiente.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

1. Fork este repositório.
2. Crie uma nova branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.
