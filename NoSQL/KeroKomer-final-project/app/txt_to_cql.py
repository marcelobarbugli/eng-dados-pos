import os

def merge_txt_files_to_cql(directory):
    # Define o caminho do arquivo de saída
    output_file_path = os.path.join(directory, "insert_statement.cql")

    # Ordem específica dos arquivos
    file_order = [
        "usuario_insert_statements.txt",
        "restaurante_insert_statements.txt",
        "cardapio_insert_statements.txt",
        "pedido_insert_statements.txt",
        "entrega_insert_statements.txt",
        "agregVendas_insert_statements.txt",
        "agregRestaurante_insert_statements.txt",
        "agregEntregadores_insert_statements.txt"
    ]

    # Abre o arquivo de saída no modo de escrita
    with open(output_file_path, 'w', encoding='utf-8', errors='ignore') as output_file:
        # Percorre os arquivos na ordem especificada
        for filename in file_order:
            file_path = os.path.join(directory, filename)
            # Verifica se o arquivo existe no diretório
            if os.path.isfile(file_path):
                # Abre o arquivo de entrada no modo de leitura
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
                        # Lê todas as linhas do arquivo de entrada e escreve no arquivo de saída
                        for line in input_file:
                            output_file.write(line)
                except Exception as e:
                    print(f"Erro ao ler o arquivo {file_path}: {e}")
            else:
                print(f"Arquivo {file_path} não encontrado.")
    
    print(f"Todos os arquivos .txt foram mesclados em {output_file_path}")

# Exemplo de uso
directory_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\assets'
merge_txt_files_to_cql(directory_path)
