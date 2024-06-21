<!-- CONTENT -->

<div class="step-title">Connect to Cassandra and create a keyspace</div>

✅ Start Cassandra:
```
./cassandra
```

✅ Start the CQL shell:
```
cqlsh
```

✅ Create the `kerokomer_key` keyspace:
```
CREATE KEYSPACE kerokomer_key
WITH replication = {
  'class': 'NetworkTopologyStrategy', 
  'DC-Houston': 1 };
```

✅ Set the current working keyspace:
```
USE kerokomer_key;
```

