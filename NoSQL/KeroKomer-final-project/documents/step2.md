<!-- CONTENT -->

<div class="step-title">Create tables</div>


✅ Create table `usuarios`:
```
CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id UUID PRIMARY KEY,
    cpf TEXT
    nome TEXT,
    email TEXT,
    senha TEXT,
    endereco TEXT,
    telefone TEXT,
    tipo TEXT,
    avaliacao TEXT
);
```

✅ Create table `restaurantes`:
```
CREATE TABLE IF NOT EXISTS restaurantes (
    restaurante_id UUID PRIMARY KEY,
    nome TEXT,
    endereco TEXT,
    telefone TEXT,
    categoria TEXT,
    proprietario_id UUID
);
```

✅ Create table `cardapio`:
```
CREATE TABLE IF NOT EXISTS cardapio(
    restaurante_id UUID,
    item_id UUID,
    nome TEXT,
    descricao TEXT,
    preco DECIMAL,
    disponibilidade BOOLEAN,
    PRIMARY KEY (restaurante_id, item_id)
);
```

✅ Create table `pedidos`:
```
CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id UUID PRIMARY KEY,
    cliente_id UUID,
    restaurante_id UUID,
    data_hora_pedido TIMESTAMP,
    status TEXT,
    total DECIMAL,
    itens MAP<TEXT, INT>
);
```

✅ Create table `entregas`:
```
CREATE TABLE IF NOT EXISTS entregas (
    entrega_id UUID PRIMARY KEY,
    pedido_id UUID,
    entregador_id UUID,
    status TEXT,
    hora_aceitacao TIMESTAMP,
    hora_conclusao TIMESTAMP
);
```

✅ Create table `agregados_entregadores`:
```
CREATE TABLE IF NOT EXISTS agregados_entregadores (
    entregador_id UUID PRIMARY KEY,
    nome TEXT,
    total_entregas INT
);
```

✅ Create table `agregados_vendas`:
```
CREATE TABLE IF NOT EXISTS agregados_vendas (
    item_id UUID PRIMARY KEY,
    nome TEXT,
    quantidade_total INT
);
```

✅ Create table `agregados_avaliacoes_restaurantes`:
```
CREATE TABLE IF NOT EXISTS agregados_avaliacoes_restaurantes (
    restaurante_id UUID PRIMARY KEY,
    nome TEXT,
    avaliacao_media DECIMAL,
    total_avaliacoes INT
);
```

✅ Verify that the tables and materialized view have been created:
```
DESCRIBE SCHEMA;
```
