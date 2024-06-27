import os
import random
import string
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# Funções gerais
def generate_random_id(length=6):
    lower_bound = 10**(length-1)
    upper_bound = (10**length) - 1
    return random.randint(lower_bound, upper_bound)

def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Gerar usuários
def generate_usuario_statements(num_records):
    statements = []
    user_ids = []
    entregador_ids = []

    tipo_quantidades = {
        'Restaurante': 10,
        'Entregador': 45,
        'Administrador': 10,
        'Usuario': num_records - 65
    }

    tipos = []
    for tipo, quantidade in tipo_quantidades.items():
        tipos.extend([tipo] * quantidade)
    
    random.shuffle(tipos)

    for i in range(1, num_records + 1):
        user_id = generate_random_id()
        user_ids.append(user_id)
        if tipos[i-1] == 'Entregador':
            entregador_ids.append(user_id)
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
    
    return statements, user_ids, entregador_ids

# Gerar restaurantes
def generate_restaurante_statements(user_ids):
    statements = []
    restaurante_ids = []
    restaurantes_rates = []

    proprietarios = random.sample(user_ids, 10)
    for i in range(1, 11):
        restaurante_id = generate_random_id()
        restaurante_ids.append(restaurante_id)
        nome = f'Restaurante {i}'
        endereco = f'Endereço {i}'
        telefone = f'1100000000{i:03d}'
        categoria = random.choice(['Italiana', 'Japonesa', 'Brasileira', 'Mexicana', 'Chinesa'])
        proprietario_id = proprietarios[i-1]
        avaliacao_media = round(random.uniform(3, 5), 1)
        total_avaliacoes = random.randint(1, 500)
        restaurantes_rates.append((restaurante_id, nome, avaliacao_media, total_avaliacoes))

        statement = f"INSERT INTO restaurantes (restaurante_id, nome, endereco, telefone, categoria, proprietario_id) VALUES ('{restaurante_id}', '{nome}', '{endereco}', '{telefone}', '{categoria}', '{proprietario_id}');"
        statements.append(statement)
    
    return statements, restaurante_ids, restaurantes_rates

# Gerar cardápio
def generate_cardapio_statements(restaurante_ids):
    statements = []
    cardapio_data = []

    for i in range(1, 201):
        restaurante_id = random.choice(restaurante_ids)
        item_id = generate_random_id(3)
        nome = f'Item {i}'
        descricao = f'Descricao do item {i}'
        preco = round(random.uniform(10, 100), 2)
        disponibilidade = random.choices([True, False], weights=[75, 25], k=1)[0]
        cardapio_data.append((restaurante_id, item_id, preco))

        statement = f"INSERT INTO cardapio (restaurante_id, item_id, nome, descricao, preco, disponibilidade) VALUES ('{restaurante_id}', '{item_id}', '{nome}', '{descricao}', {preco}, {disponibilidade});"
        statements.append(statement)
    
    return statements, cardapio_data

# Gerar pedidos
def generate_pedido_statements(num_records, cardapio_data, user_ids):
    statements = []
    pedidos_ids = []
    pedidos_ids_for_entregas = []
    vendas_soma = defaultdict(int)

    # Ajustar o número de pedidos para não exceder o número de usuários
    num_records = min(num_records, len(user_ids))
    
    cliente_ids = random.sample(user_ids, num_records)
    status_options = ['Pending', 'In Progress', 'Completed', 'Cancelled']
    start_date = datetime.now() - timedelta(days=365)

    for i in range(1, num_records + 1):
        pedido_id = generate_random_id(8)
        pedidos_ids.append(pedido_id)
        cliente_id = cliente_ids[i-1]
        restaurante_id, item_id, preco = random.choice(cardapio_data)
        data_hora_pedido = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        status = random.choice(status_options)
        if status in ['In Progress', 'Completed']:
            pedidos_ids_for_entregas.append(pedido_id)
        if status in ['In Progress', 'Completed', 'Pending']:
            vendas_soma[(item_id, f'Item {item_id}')] += random.randint(1, 10)
        itens = {item_id: random.randint(1, 10)}
        total = sum(quantity * preco for quantity in itens.values())
        itens_str = '{' + ', '.join([f"'{k}': {v}" for k, v in itens.items()]) + '}'

        statement = f"INSERT INTO pedidos (pedido_id, cliente_id, restaurante_id, data_hora_pedido, status, total, itens) VALUES ({pedido_id}, {cliente_id}, '{restaurante_id}', '{data_hora_pedido}', '{status}', {total}, {itens_str});"
        statements.append(statement)
    
    return statements, pedidos_ids, pedidos_ids_for_entregas, vendas_soma

# Gerar entregas
def generate_entrega_statements(pedidos_ids_for_entregas, entregadores):
    statements = []
    start_date = datetime.now() - timedelta(days=365)
    entregas_count = Counter()

    for pedido_id in pedidos_ids_for_entregas:
        entregador_id = random.choice(entregadores)
        entregas_count[entregador_id] += 1
        status = 'In Progress' if random.random() < 0.5 else 'Completed'
        hora_aceitacao = start_date + timedelta(minutes=random.randint(0, 525600))

        if status == 'Completed':
            hora_conclusao = hora_aceitacao + timedelta(minutes=50)
        else:
            hora_conclusao = None

        hora_conclusao_str = f"'{hora_conclusao}'" if hora_conclusao else 'NULL'

        statement = (
            f"INSERT INTO entregas (entrega_id, pedido_id, entregador_id, status, hora_aceitacao, hora_conclusao) "
            f"VALUES ({generate_random_id(8)}, {pedido_id}, {entregador_id}, '{status}', '{hora_aceitacao}', {hora_conclusao_str});"
        )
        statements.append(statement)

    return statements, entregas_count

# Gerar agregados de vendas
def generate_agregados_vendas_statements(vendas_soma):
    statements = []
    start_date = datetime.now() - timedelta(days=365)
    hora_aceitacao = start_date + timedelta(minutes=random.randint(0, 525600))
    for key, quantidade_total in vendas_soma.items():
        if len(key) == 3:
            item_id, hora_aceitacao, nome = key
            statement = (
                f"INSERT INTO agregados_vendas_by_quantidade (date, item_id, nome_item, quantidade_total) "
                f"VALUES ({hora_aceitacao}, {item_id}, '{nome}', {quantidade_total});"
            )
        elif len(key) == 2:
            item_id, nome = key
            statement = (
                f"INSERT INTO agregados_vendas_by_quantidade (date, item_id, nome, quantidade_total) "
                f"VALUES ({hora_aceitacao}, {item_id}, '{nome}', {quantidade_total});"
            )
        else:
            raise ValueError("Unexpected key length in vendas_soma")
        
        statements.append(statement)
    return statements

# Gerar agregados de avaliações de restaurantes
def generate_agregados_restaurantes_statements(num_records, restaurantes_rates):
    statements = set()  # Use a set para evitar duplicatas
    while len(statements) < num_records:
        restaurante_id, nome, avaliacao_media, total_avaliacoes = random.choice(restaurantes_rates)
        statement = (
            f"INSERT INTO agregados_avaliacoes_restaurantes (restaurante_id, nome, avaliacao_media, total_avaliacoes) "
            f"VALUES ({restaurante_id}, '{nome}', {avaliacao_media}, {total_avaliacoes});"
        )
        statements.add(statement)
    return list(statements)

# Gerar agregados de entregadores
def generate_agregados_entregadores_statements(entregas_count, entregador_ids):
    statements = []
    for entregador_id in entregador_ids:
        total_entregas = entregas_count.get(entregador_id, 0)
        nome = f'Nome{entregador_id} Sobrenome{entregador_id}'
        statement = (
            f"INSERT INTO agregados_entregadores (entregador_id, nome, total_entregas) "
            f"VALUES ({entregador_id}, '{nome}', {total_entregas});"
        )
        statements.append(statement)
    return statements

# Quantidades de registros
num_usuarios = 200
num_restaurantes = 10
num_cardapio = 200
num_pedidos = 4980
num_agregados_vendas = 148
num_agregados_restaurantes = 10
num_agregados_entregadores = 45

# Gerar os dados
usuario_statements, user_ids, entregador_ids = generate_usuario_statements(num_usuarios)
restaurante_statements, restaurante_ids, restaurantes_rates = generate_restaurante_statements(user_ids)
cardapio_statements, cardapio_data = generate_cardapio_statements(restaurante_ids)
pedido_statements, pedidos_ids, pedidos_ids_for_entregas, vendas_soma = generate_pedido_statements(num_pedidos, cardapio_data, user_ids)
entrega_statements, entregas_count = generate_entrega_statements(pedidos_ids_for_entregas, entregador_ids)
agregados_vendas_statements = generate_agregados_vendas_statements(vendas_soma)
agregados_restaurantes_statements = generate_agregados_restaurantes_statements(num_agregados_restaurantes, restaurantes_rates)
agregados_entregadores_statements = generate_agregados_entregadores_statements(entregas_count, entregador_ids)


def write_statements_to_file(statements, relative_file_path):
    # Extrai o diretório do caminho do arquivo
    directory = os.path.dirname(relative_file_path)
    
    # Cria o diretório se ele não existir
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Escreve as instruções no arquivo
    with open(relative_file_path, 'w') as file:
        for statement in statements:
            file.write(statement + '\n')

# Caminhos dos arquivos
file_paths = {
    'usuarios': r'.\data\usuario_insert_statements.txt',
    'restaurantes': r'.\data\restaurante_insert_statements.txt',
    'cardapio': r'.\data\cardapio_insert_statements.txt',
    'pedidos': r'.\data\pedido_insert_statements.txt',
    'entregas': r'.\data\entrega_insert_statements.txt',
    'agregados_vendas': r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\app\data\agregVendas_insert_statements.txt',
    'agregados_restaurantes': r'.\data\agregRestaurante_insert_statements.txt',
    'agregados_entregadores': r'.\data\agregEntregadores_insert_statements.txt'
}

# Escrever os dados para os arquivos
write_statements_to_file(usuario_statements, file_paths['usuarios'])
write_statements_to_file(restaurante_statements, file_paths['restaurantes'])
write_statements_to_file(cardapio_statements, file_paths['cardapio'])
write_statements_to_file(pedido_statements, file_paths['pedidos'])
write_statements_to_file(entrega_statements, file_paths['entregas'])
write_statements_to_file(agregados_vendas_statements, file_paths['agregados_vendas'])
write_statements_to_file(agregados_restaurantes_statements, file_paths['agregados_restaurantes'])
write_statements_to_file(agregados_entregadores_statements, file_paths['agregados_entregadores'])
