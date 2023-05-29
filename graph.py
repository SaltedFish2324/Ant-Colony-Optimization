import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.distances = None

    def calculate_distances(self, graph):
        distances = np.zeros((self.num_nodes, self.num_nodes))
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                distances[i][j] = distances[j][i] = np.linalg.norm(np.array(graph[i]) - np.array(graph[j]))
        self.distances = distances

    def visualize_graph(self, graph):
        G = nx.Graph()
        for i in range(self.num_nodes):
            G.add_node(i, pos=(graph[i][0], graph[i][1]))
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                G.add_edge(i, j, weight=self.distances[i][j])
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
