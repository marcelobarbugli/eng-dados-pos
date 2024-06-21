<div class="step-title">Design update</div>

✅ Adicionar um pedido Pedido  `69582783` e realizando um update no subtotal do Pedido para `199.75`:


```
BEGIN BATCH
  INSERT INTO pedidos (
    pedido_id,
    cliente_id,
    restaurante_id,
    data_hora_pedido,
    status,
    total,
    itens)
  VALUES (69582783, 
  690628, 
  '772186', 
  '2024-06-20 11:36:05.579212', 
  'In Progress', 
  469.75, 
  {'494': 5});
  UPDATE items_by_cart 
  SET total = 199.75
  WHERE pedido_id = 69582783
  IF total = 469.75;
APPLY BATCH;

SELECT pedido_id, cliente_id, itens, 
       total 
FROM pedidos
WHERE pedido_id = 69582783; 
```


