import random
import string

def generate_random_id(length=3):
    lower_bound = 10**(length-1)
    upper_bound = (10**length) - 1
    return random.randint(lower_bound, upper_bound)

def generate_insert_statements(num_records):
    restaurante_ids = [
        '549469', '516536', '202305', '897122', 
        '216182', '161763', '365193', '882689', 
        '400851', '856996'
    ]
    
    statements = []
    for i in range(1, num_records + 1):
        restaurante_id = random.choice(restaurante_ids)
        item_id = generate_random_id()
        nome = f'Item {i}'
        descricao = f'Descricao do item {i}'
        preco = round(random.uniform(10, 100), 2)
        disponibilidade = random.choices([True, False], weights=[75, 25], k=1)[0]

        statement = f"INSERT INTO cardapio (restaurante_id, item_id, nome, descricao, preco, disponibilidade) VALUES ('{restaurante_id}', '{item_id}', '{nome}', '{descricao}', {preco}, {disponibilidade});"
        statements.append(statement)
    
    return statements

num_records = 200
insert_statements = generate_insert_statements(num_records)

file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\cardapio_insert_statements.txt'
with open(file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
