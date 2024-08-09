
# Exercício 2 - Ingestão de Dados

Este repositório contém o código e a documentação para o **Exercício 2** da disciplina de Ingestão de Dados do curso de Engenharia de Dados.

## Objetivo

O objetivo deste exercício é desenvolver uma pipeline de ingestão de dados utilizando ferramentas e técnicas de engenharia de dados utlizando apenas Python. O pipeline deve ser capaz de extrair, transformar e carregar (ETL) dados para um destino, garantindo a qualidade e integridade dos dados.

## Estrutura do Repositório

- **`analyse/`**: Contém Query de consultas.
- **`data/`**: Contém os arquivos de dados utilizados para o exercício (bronze/, silver/, gold/).
- **`extractCSV/`**: Contém scripts Python para automatização das tarefas de ETL - extração.
- **`TransformLoad/`**: Contém scripts de teste para validação das transformações e cargas de dados - transformação e load no SQLite.
- **`config`**: Contém script de criação do db, insert no banco a partir do file na camada gold.
- **`Dados/`**: Contém dados em CSV e TSV para o desenvolvimento do exercício.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolvimento dos scripts.
- **SQLite**: Utilizado criação do banco de dados e análise de dados estruturados.

## Como Executar

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/marcelobarbugli/eng-dados-pos.git
   cd eng-dados-pos/ingestao-de-dados/Exercicio2
   ```

2. Execute scripts nessa sequencia. Para rodar os scripts Python diretamente:

   ```bash
   python extractCSV/extract_bancos.py
   python extractCSV/extract_empregados.py
   python extractCSV/extract_reclamacoes.py
   python TransformLoad/transform_bancos.py
   python TransformLoad/transform_empregados.py
   python TransformLoad/transform_reclamacoes.py
   python TransformLoad/load.py
   ```

3. Para criar db, tabela, views e análise:

   ```bash
   python config/db.py
   python analyse/create_view.py
   python analyse/select_from_table.py
   ```

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests para contribuir com melhorias ou correções.

