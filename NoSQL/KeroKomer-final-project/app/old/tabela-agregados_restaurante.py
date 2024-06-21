import random

def generate_insert_statements(num_records, restaurantes_rates):
    statements = set()  # Use a set to avoid duplicates
    while len(statements) < num_records:
        restaurante_id, nome, avaliacao_media, total_avaliacoes = random.choice(restaurantes_rates)
        statement = (
            f"INSERT INTO agregados_avaliacoes_restaurantes (restaurante_id, nome, avaliacao_media, total_avaliacoes) "
            f"VALUES ({restaurante_id}, '{nome}', {avaliacao_media}, {total_avaliacoes});"
        )
        statements.add(statement)
    return list(statements)

num_records = 10
restaurantes_rates = [
    ('549469', 'Restaurante 1', 4.4, 48), ('516536', 'Restaurante 2', 3.3, 110), ('202305', 'Restaurante 3', 3.8, 540), ('897122', 'Restaurante 4', 4.6, 11), ('216182', 'Restaurante 5', 3.2, 59), ('161763', 'Restaurante 6', 4.6, 201), ('365193', 'Restaurante 7', 4.9, 3), ('882689', 'Restaurante 8', 3, 1), ('400851', 'Restaurante 9', 4, 78), ('856996', 'Restaurante 10', 3.4, 2)
]

insert_statements = generate_insert_statements(num_records, restaurantes_rates)

output_file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\agregRestaurante_insert_statements.txt'
with open(output_file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
