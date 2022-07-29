import networkx as nx

import main

terminals = 30
color_map = []
G1 = nx.fast_gnp_random_graph(50, 0.3)

for i in range(0, len(G1)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

pos_G1 = nx.random_layout(G1)
nx.draw(G1, pos=pos_G1, with_labels=True)

main.sph(G1, pos_G1, terminals)
main.algorithm(G1, pos_G1, terminals)
main.algorithm2(G1, pos_G1, terminals)
main.algorithm3(G1, pos_G1, terminals)