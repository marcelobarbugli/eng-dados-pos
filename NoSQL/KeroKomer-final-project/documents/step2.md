<!-- CONTENT -->

<div class="step-title">Create tables</div>


✅ Create table `usuarios`:
```
CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id INT,
    cpf TEXT,
    nome TEXT,
    email TEXT,
    senha TEXT,
    endereco TEXT,
    telefone TEXT,
    tipo TEXT,
    avaliacao TEXT,
    PRIMARY KEY (usuario_id, cpf)
);
```

✅ Create table `restaurantes`:
```
CREATE TABLE IF NOT EXISTS restaurantes (
    restaurante_id INT,
    nome TEXT,
    endereco TEXT,
    telefone TEXT,
    categoria TEXT,
    proprietario_id INT,
    PRIMARY KEY (restaurante_id, proprietario_id)
);
```

✅ Create table `cardapio`:
```
CREATE TABLE IF NOT EXISTS cardapio(
    item_id INT,
    restaurante_id INT,
    nome TEXT,
    descricao TEXT,
    preco DECIMAL,
    disponibilidade BOOLEAN,
    PRIMARY KEY (item_id, restaurante_id)
);
```

✅ Create table `pedidos`:
```
CREATE TABLE pedidos (
    pedido_id INT,
    cliente_id INT,
    restaurante_id INT,
    data_hora_pedido TIMESTAMP,
    status TEXT,
    total DECIMAL,
    itens MAP<TEXT, INT>,
    PRIMARY KEY (pedido_id, cliente_id, restaurante_id)
);
```

✅ Create table `entregas`:
```
CREATE TABLE IF NOT EXISTS entregas (
    entrega_id INT,
    pedido_id INT,
    entregador_id INT,
    status TEXT,
    hora_aceitacao TIMESTAMP,
    hora_conclusao TIMESTAMP,
    PRIMARY KEY (entrega_id, pedido_id, entregador_id)
);
```

✅ Create table `agregados_entregadores`:
```
CREATE TABLE IF NOT EXISTS agregados_entregadores (
    tipo TEXT,
    nome TEXT,
    total_entregas INT,
    PRIMARY KEY ((tipo), total_entregas)
)    WITH CLUSTERING ORDER BY (
    total_entregas ASC
);
```

✅ Create table `agregados_vendas`:
```
CREATE TABLE IF NOT EXISTS agregados_vendas_by_quantidade (
    date TEXT,
    item_id INT,
    nome TEXT,
    quantidade_total INT,
    PRIMARY KEY ((date), quantidade_total)
) WITH CLUSTERING ORDER BY (quantidade_total DESC);
```


✅ Create table `agregados_avaliacoes_restaurantes`:
```
CREATE TABLE IF NOT EXISTS agregados_avaliacoes_restaurantes (
    tipo TEXT,
    restaurante_id INT,
    nome TEXT,
    avaliacao_media DECIMAL,
    total_avaliacoes INT,
    PRIMARY KEY ((tipo), avaliacao_media, total_avaliacoes), 
) WITH CLUSTERING ORDER BY (
    avaliacao_media DESC,
    total_avaliacoes DESC
);
```

✅ Verify that the tables and materialized view have been created:
```
DESCRIBE SCHEMA;
```
