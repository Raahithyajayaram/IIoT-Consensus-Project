from dag_layer.dag import DAG

dag = DAG()

# Add sample transactions
genesis = dag.add_transaction("Genesis TX")
tx1 = dag.add_transaction("Sensor reading A", parents=[genesis])
tx2 = dag.add_transaction("Sensor reading B", parents=[genesis])
tx3 = dag.add_transaction("Sensor reading C", parents=[tx1, tx2])

dag.visualize()
