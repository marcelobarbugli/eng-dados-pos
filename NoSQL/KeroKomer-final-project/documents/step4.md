<div class="step-title">Design Queries:</div>



✅ Consultar Restaurantes por `Categoria`:
```
SELECT * FROM restaurantes WHERE categoria = 'Brasileira' ALLOW FILTERING;        
```

✅ Consultar Itens de Menu de um Restaurante:
```
SELECT * FROM cardapio WHERE restaurante_id = (543884) ALLOW FILTERING;
```

✅ Consultar `Pedidos` de um  `Cliente`:
```
SELECT * FROM pedidos WHERE cliente_id = (922304) ALLOW FILTERING;                   
```

✅ Consultar Entregas finalizadas de um Entregador:
```
SELECT entrega_id, pedido_id, entregador_id, status FROM entregas WHERE entregador_id = (384201) AND status = 'Completed' ALLOW FILTERING;
```

✅ Consultar Informações de um `Usuário`:
```
SELECT * FROM usuarios WHERE usuario_id = (125611) ALLOW FILTERING;
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
SELECT * FROM pedidos WHERE pedido_id = (78435300) ALLOW FILTERING;
```

✅ Consultar Usuário por `CPF`:
```
SELECT * FROM usuarios WHERE cpf = '10000000025' ALLOW FILTERING;
```

✅ Consultar Pedidos de um Restaurante:
```
SELECT * FROM pedidos WHERE restaurante_id = (543884) ALLOW FILTERING;
```

✅ Consultar Itens Mais Vendidos:
```
SELECT * FROM agregados_vendas_by_quantidade WHERE date = '2024-01-30' limit 10;
```

✅ Consulta para Top 10 Entregadores:
```
SELECT * FROM agregados_entregadores  WHERE tipo = 'entregador' ORDER BY total_entregas DESC ALLOW FILTERING;
```

✅ Consulta para Top 10 Restaurantes:
```
SELECT * FROM agregados_avaliacoes_restaurantes WHERE tipo = 'restaurante' ORDER BY avaliacao_media, total_avaliacoes LIMIT 5 ALLOW FILTERING;
```