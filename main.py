from itertools import combinations, groupby
import random
import networkx as nx
import matplotlib.pyplot as plt


terminals = 6
color_map = []
G1 = nx.fast_gnp_random_graph(18,0.1)
for node in G1:
    if node < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

pos_G1 = nx.random_layout(G1)
print(pos_G1)
print(pos_G1[0])

nx.draw(G1, node_color=color_map, node_size=800, pos=pos_G1, with_labels=True)
plt.show()

