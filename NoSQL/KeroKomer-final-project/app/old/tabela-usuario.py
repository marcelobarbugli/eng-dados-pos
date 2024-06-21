import random

def generate_random_id(length=6):
    lower_bound = 10**(length-1)
    upper_bound = (10**length) - 1
    return random.randint(lower_bound, upper_bound)

def generate_insert_statements(num_records):
    statements = []
    
    # Quantidades específicas de cada tipo
    tipo_quantidades = {
        'Restaurante': 10,
        'Entregador': 45,
        'Administrador': 10,
        'Usuario': num_records - 65  # O restante será do tipo Usuarios
    }
    
    # Criação dos tipos de usuários
    tipos = []
    for tipo, quantidade in tipo_quantidades.items():
        tipos.extend([tipo] * quantidade)
    
    random.shuffle(tipos)  # Embaralha os tipos para distribuição aleatória

    for i in range(1, num_records + 1):
        user_id = generate_random_id()
        cpf = f'{10000000000 + i:011d}'
        nome = f'Nome{i} Sobrenome{i}'
        email = f'nome{i}.sobrenome{i}@example.com'
        senha = f'senha{i:03d}'
        endereco = f'Endereco {i}'
        telefone = f'{55250000000 + i:011d}'
        tipo = tipos[i-1]
        avaliacao = round(random.uniform(3, 5), 1) if tipo in ['Restaurante', 'Entregador'] else 'NULL'
        
        statement = f"INSERT INTO usuarios (user_ID, CPF, nome, email, senha, endereco, telefone, tipo, avaliacao) VALUES ('{user_id}', '{cpf}', '{nome}', '{email}', '{senha}', '{endereco}', '{telefone}', '{tipo}', {avaliacao});"
        statements.append(statement)
    
    return statements

num_records = 200
insert_statements = generate_insert_statements(num_records)

file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\usuario_insert_statements.txt'
with open(file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
