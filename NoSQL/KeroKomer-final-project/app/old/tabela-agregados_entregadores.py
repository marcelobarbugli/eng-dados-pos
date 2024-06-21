import random

def generate_insert_statements(num_records, entregador_soma):
    statements = []
    for _ in range(num_records):
        entregador_id, nome, total_entregas = random.choice(entregador_soma)
        statement = (
            f"INSERT INTO agregados_entregadores (entregador_id, nome, total_entregas) "
            f"VALUES ({entregador_id}, '{nome}', {total_entregas});"
        )
        statements.append(statement)
    return statements

num_records = 45
entregador_soma = [
    ('812358', 'Nome4 Sobrenome4', 115), ('356136', 'Nome7 Sobrenome7', 125),
    ('502854', 'Nome22 Sobrenome22', 112), ('437109', 'Nome23 Sobrenome23', 105),
    ('538141', 'Nome25 Sobrenome25', 119), ('995329', 'Nome31 Sobrenome31', 91),
    ('103638', 'Nome32 Sobrenome32', 115), ('118135', 'Nome33 Sobrenome33', 124),
    ('709925', 'Nome34 Sobrenome34', 112), ('974709', 'Nome37 Sobrenome37', 106),
    ('509089', 'Nome42 Sobrenome42', 93), ('206680', 'Nome43 Sobrenome43', 106),
    ('161174', 'Nome52 Sobrenome52', 107), ('322061', 'Nome57 Sobrenome57', 97),
    ('602461', 'Nome58 Sobrenome58', 97), ('579127', 'Nome59 Sobrenome59', 120),
    ('491707', 'Nome60 Sobrenome60', 108), ('138528', 'Nome63 Sobrenome63', 114),
    ('499720', 'Nome69 Sobrenome69', 124), ('300606', 'Nome82 Sobrenome82', 113),
    ('133689', 'Nome91 Sobrenome91', 100), ('589694', 'Nome95 Sobrenome95', 113),
    ('978846', 'Nome96 Sobrenome96', 109), ('777768', 'Nome100 Sobrenome100', 100),
    ('174581', 'Nome103 Sobrenome103', 99), ('962397', 'Nome106 Sobrenome106', 106),
    ('463145', 'Nome109 Sobrenome109', 124), ('670719', 'Nome110 Sobrenome110', 118),
    ('347793', 'Nome114 Sobrenome114', 106), ('805310', 'Nome119 Sobrenome119', 113),
    ('882666', 'Nome122 Sobrenome122', 114), ('643380', 'Nome131 Sobrenome131', 96),
    ('795611', 'Nome135 Sobrenome135', 116), ('182064', 'Nome138 Sobrenome138', 111),
    ('759850', 'Nome156 Sobrenome156', 113), ('307224', 'Nome157 Sobrenome157', 127),
    ('557849', 'Nome159 Sobrenome159', 103), ('754447', 'Nome164 Sobrenome164', 103),
    ('298232', 'Nome167 Sobrenome167', 121), ('616687', 'Nome171 Sobrenome171', 118),
    ('615126', 'Nome172 Sobrenome172', 113), ('245622', 'Nome183 Sobrenome183', 124),
    ('463214', 'Nome188 Sobrenome188', 109), ('685930', 'Nome192 Sobrenome192', 115),
    ('973965', 'Nome198 Sobrenome198', 106)
]

insert_statements = generate_insert_statements(num_records, entregador_soma)

output_file_path = r'C:\Users\010441631\Documents\GitHub\eng-dados-pos\eng-dados-pos\NoSQL\KeroKomer-final-project\data\agregEntregadores_insert_statements.txt'
with open(output_file_path, 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')
