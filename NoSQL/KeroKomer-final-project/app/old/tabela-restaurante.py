import random
import string

def generate_random_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_insert_statements(num_records):
    statements = []
    for i in range(1, num_records + 1):
        restaurante_id = generate_random_id()
        nome = f'Restaurante {i}'
        endereco = f'Endereço {i}'
        telefone = f'1100000000{i:03d}'
        categoria = random.choice(['Italiana', 'Japonesa', 'Brasileira', 'Mexicana', 'Chinesa'])
        proprietario_id = f'{55250000000 + i:011d}'

        statement = f"INSERT INTO restaurantes (restaurante_id, nome, endereco, telefone, categoria, proprietario_id) VALUES ('{restaurante_id}', '{nome}', '{endereco}', '{telefone}', '{categoria}', '{proprietario_id}');"
        statements.append(statement)
    
    return statements

num_records = 10
insert_statements = generate_insert_statements(num_records)

file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\restaurante_insert_statements.txt'
with open(file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
