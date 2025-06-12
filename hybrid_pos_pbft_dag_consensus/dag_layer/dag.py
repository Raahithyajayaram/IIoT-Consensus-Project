import networkx as nx
import uuid
import time

class DAG:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_transaction(self, data, parents=[]):
        tx_id = str(uuid.uuid4())
        timestamp = time.time()
        self.graph.add_node(tx_id, data=data, timestamp=timestamp)

        if not parents:  # Genesis transaction
            self.graph.add_edge("GENESIS", tx_id)
        else:
            for parent in parents:
                if parent in self.graph.nodes:
                    self.graph.add_edge(parent, tx_id)

        return tx_id

    def get_parents(self, tx_id):
        return list(self.graph.predecessors(tx_id))

    def get_all_transactions(self):
        return list(self.graph.nodes(data=True))

    def visualize(self):
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=800, node_color="skyblue")
        plt.title("DAG Structure of Transactions")
        plt.show()
