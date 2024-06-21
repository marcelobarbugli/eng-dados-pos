<div class="step-title">Design Queries:</div>



✅ Consultar Restaurantes por `Categoria`:
```
SELECT * FROM restaurantes WHERE categoria = 'Brasileira' ALLOW FILTERING;        
```

✅ Consultar Itens de Menu de um Restaurante:
```
SELECT * FROM cardapio WHERE restaurante_id = uuid(549469);
```

✅ Consultar `Pedidos` de um  `Cliente`:
```
SELECT * FROM pedidos WHERE cliente_id = uuid(624040) ALLOW FILTERING;                   
```

✅ Consultar Entregas finalizadas de um Entregador:
```
SELECT entrega_id, pedido_id, entregador_id, status FROM entregas WHERE entregador_id = uuid(502854) AND status = 'Completed' ALLOW FILTERING;
```

✅ Consultar Informações de um `Usuário`:
```
SELECT * FROM usuarios WHERE usuario_id = uuid(624040);
```

✅ Consultar `Pedidos` por `Status`:
```
SELECT * FROM pedidos WHERE status = 'Pending' ALLOW FILTERING;
```

✅ Consultar Todos os `Itens` de Menu Disponíveis:
```
SELECT * FROM cardapio WHERE disponibilidade = true ALLOW FILTERING;
```

✅ Consultar Detalhes de um `Pedido` Específico:
```
SELECT * FROM pedidos WHERE pedido_id = uuid(60631759);
```

✅ Consultar Usuário por `CPF`:
```
SELECT * FROM usuarios WHERE cpf = 10000000025 ALLOW FILTERING;
```

✅ Consultar Pedidos de um Restaurante:
```
SELECT * FROM pedidos WHERE restaurante_id = uuid(216182) ALLOW FILTERING;
```

✅ Consultar Itens Mais Vendidos:
```
SELECT * FROM agregados_vendas ORDER BY quantidade_total DESC;
```

✅ Consulta para Top 10 Entregadores:
```
SELECT * FROM agregados_entregadores ORDER BY total_entregas DESC LIMIT 10;
```

✅ Consulta para Top 10 Restaurantes:
```
SELECT * FROM agregados_avaliacoes_restaurantes ORDER BY avaliacao_media DESC LIMIT 10;
```