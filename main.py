from itertools import combinations, groupby
import random
import networkx as nx
import matplotlib.pyplot as plt

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G

terminals = 6
color_map = []
G1 = gnp_random_connected_graph(18,0.1)
for node in G1:
    if node < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

pos_G1 = nx.random_layout(G1)
nx.draw(G1, node_color=color_map, node_size=800, pos=pos_G1, with_labels=True)
plt.show()

