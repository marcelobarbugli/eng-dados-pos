import random
import string
from datetime import datetime, timedelta

def generate_random_id(length=6):
    lower_bound = 10**(length-1)
    upper_bound = (10**length) - 1
    return random.randint(lower_bound, upper_bound)

def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_items(num_items=5):
    items = {}
    for _ in range(num_items):
        item_id = generate_random_string(6)
        quantity = random.randint(1, 10)
        items[item_id] = quantity
    return items

def parse_pedido_file(file_path):
    pedido_ids = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split('VALUES')
                pedido_values = parts[1].strip().strip('();').split(',')
                pedido_id = int(pedido_values[0].strip())
                pedido_ids.append(pedido_id)
    return pedido_ids

def generate_insert_statements(num_records, pedido_ids, entregadores):
    statements = []
    status_options = ['Pending', 'In Progress', 'Completed', 'Cancelled']
    start_date = datetime.now() - timedelta(days=365)

    for i in range(1, num_records + 1):
        pedido_id = random.choice(pedido_ids)
        entregador_id = random.choice(entregadores)
        status = random.choice(status_options)
        hora_aceitacao = start_date + timedelta(minutes=random.randint(0, 525600))  # 365 days * 1440 minutes/day
        
        if status == 'Completed':
            hora_conclusao = hora_aceitacao + timedelta(minutes=50)
        elif status == 'Cancelled':
            hora_conclusao = hora_aceitacao + timedelta(minutes=10)
        else:
            hora_conclusao = None

        hora_conclusao_str = f"'{hora_conclusao}'" if hora_conclusao else 'NULL'

        statement = (
            f"INSERT INTO entregas (entrega_id, pedido_id, entregador_id, status, hora_aceitacao, hora_conclusao) "
            f"VALUES ({generate_random_id(8)}, {pedido_id}, {entregador_id}, '{status}', '{hora_aceitacao}', {hora_conclusao_str});"
        )
        statements.append(statement)

    return statements

# Lista de entregadores
entregadores = [
    '812358', '356136', '502854', '437109', '538141', '995329', '103638', '118135', 
    '709925', '974709', '509089', '206680', '161174', '322061', '602461', '579127', 
    '491707', '138528', '499720', '300606', '133689', '589694', '978846', '777768', 
    '174581', '962397', '463145', '670719', '347793', '805310', '882666', '643380', 
    '795611', '182064', '759850', '307224', '557849', '754447', '298232', '616687', 
    '615126', '245622', '463214', '685930', '973965'
]

pedido_file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\pedido_insert_statements.txt'
pedido_ids = parse_pedido_file(pedido_file_path)

num_records = 4980
insert_statements = generate_insert_statements(num_records, pedido_ids, entregadores)

output_file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\entrega_insert_statements.txt'
with open(output_file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
